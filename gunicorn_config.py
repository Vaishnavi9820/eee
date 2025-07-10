# gunicorn_config.py
# Configuration for Gunicorn
import multiprocessing

# Number of workers = (2 x number of CPU cores) + 1
workers = 1  # Reduced for Render's free tier
worker_class = 'sync'
timeout = 120
keepalive = 5
max_requests = 1000
max_requests_jitter = 100
