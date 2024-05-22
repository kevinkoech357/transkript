# Define the Gunicorn configuration settings

# Server Socket
bind = "0.0.0.0:8003"
backlog = 2048

# Worker Processes
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 1000
keepalive = 7
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "access.log"
errorlog = "error.log"
loglevel = "info"
