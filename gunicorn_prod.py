import multiprocessing
import os

# Server socket
bind = "0.0.0.0:" + os.environ.get("PORT", "10000")

# Worker processes
workers = 1
worker_class = "sync"
worker_connections = 1000
timeout = 120
keepalive = 5

# Logging
loglevel = "debug"
accesslog = "-"  # Log to stdout
errorlog = "-"  # Log to stderr
capture_output = True

# Server mechanics
max_requests = 1000
max_requests_jitter = 50

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190
