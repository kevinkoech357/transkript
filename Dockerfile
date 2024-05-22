# Stage 1: Init
FROM python:3.11 AS init

# Install `uv` for faster package bootstrapping
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Set the working directory in the container
WORKDIR /app

# Copy only requirements to leverage Docker cache
COPY requirements.txt .

# Install system dependencies and create virtual environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    python3-dev \
    gcc \
    vim \
    ffmpeg \
    gunicorn && \
    rm -rf /var/lib/apt/lists/* && \
    /root/.cargo/bin/uv venv && \
    . /app/.venv/bin/activate && \
    /root/.cargo/bin/uv pip install --system --no-cache -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Copy artifacts into slim image
FROM python:3.11-slim

# Create a non-root user
RUN adduser --disabled-password --home /app kevin

# Set the working directory and switch to non-root user
WORKDIR /app
USER kevin

# Copy files from the init stage and set permissions
COPY --chown=kevin:kevin --from=init /app /app

# Add virtual environment to PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the port on which Gunicorn will listen
EXPOSE 8003

# Command to run the Flask application using Gunicorn
CMD ["gunicorn", "-c", "gunicorn_config.py", "run:app"]
