# Transkript

Transkript is a Flask-based web application designed to transcribe audio and video files, providing downloadable transcripts for users. It utilizes the Whisper Model from OPENAI for accurate transcriptions.



https://github.com/kevinkoech357/transkript/assets/102515005/c756a12b-842c-47e3-90cd-7d95ff9ed3af



## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Audio Transcription:** Transcribe audio files to text.
- **Video Transcription:** Transcribe video files to text.
- **Downloadable Transcripts:** Users can download the transcriptions as SRT files.
- **User-Friendly Interface:** An intuitive and easy-to-use web interface for file upload.

## Getting Started

Follow these instructions to set up and run Transkript on your local machine for development or testing purposes.

### Prerequisites

- [Python](https://www.python.org/) (version 3.8+)
- ffmpeg ==> ```bash sudo apt update && sudo apt install ffmpeg -y```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kevinkoech357/transkript.git
    ```

2. Navigate to the project directory:

    ```bash
    cd transkript
    mkdir uploads

    # Create .env file and add
    UPLOAD_FOLDER='/path/to/upload/folder'
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    - On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Run the Flask backend:

    ```bash
    python3 run.py

    or 

    gunicorn -w 4 run:app
    ```

2. Visit [http://localhost:5000](http://localhost:5000) in your web browser.

### Usage

1. Upload your audio or video file using the provided form.
2. Wait for the transcription process to complete.
3. Once completed, you can download the transcription as an SRT file.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OPENAI for providing the powerful Whisper model.
