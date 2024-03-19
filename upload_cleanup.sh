#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
    source .env
else
    echo "Error: .env file not found."
    exit 1
fi

# Check if the uploads directory exists
if [ ! -d "$UPLOAD_FOLDER" ]; then
    echo "Uploads directory does not exist."
    exit 1
fi

# Change to the uploads directory
cd "$UPLOAD_FOLDER" || exit

# Delete all files in the uploads directory
find . -type f -delete

# Optionally, you can add a log message to track when the script runs
echo "All files deleted from $UPLOAD_FOLDER at $(date)" >> /var/log/upload_cleanup.log