#!/usr/bin/bash

source .venv/bin/activate

uv pip install -r requirements.txt

uv pip install setuptools-rust

gunicorn -c gunicorn_config.py run:app --reload --daemon
