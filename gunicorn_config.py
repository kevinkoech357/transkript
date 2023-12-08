limit_request_line = 0
limit_request_fields = 32768
limit_request_field_size = 0
limit_request_body = 52428800  # 50 MB in bytes

bind = "0.0.0.0:8000"
workers = 3
loglevel = "debug"
accesslog = "gunicorn_access.log"
errorlog = "gunicorn_error.log"
timeout = 300
