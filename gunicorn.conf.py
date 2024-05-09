from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

bind = "0.0.0.0:8000"
workers = 2
threads = 1

loglevel = 'INFO' 
capture_output = True
 
# Redirect standard output and error streams to separate logs
accesslog = f'{BASE_DIR}/aawscicd/logs/gunicorn_access.log'
errorlog = f'{BASE_DIR}/aawscicd/logs/gunicorn_error.log'
