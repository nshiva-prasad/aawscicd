import logging.config
import inspect
import time
import logging
from decouple import config

from pathlib import Path


LOG_LEVEL = config('LOG_LEVEL')

BASE_DIR = Path(__file__).resolve().parent.parent

LOGGING_CONFIG = None


class ExceptionFilter(logging.Filter):
    def filter(self, record):
        logger_name = record.name
        return (
            record.levelno != logging.DEBUG or
            'Exception while resolving variable' in record.getMessage()
        ) and not (logger_name.startswith('kombu.') or logger_name.startswith('flower.'))


class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        created = record.created
        milliseconds = int((created - int(created)) * 1000)
        ct = self.converter(created)
        t = time.strftime('%Y-%m-%d %H:%M:%S', ct)
        return '%s:%03d' % (t, milliseconds)

    def format(self, record):
        stack = inspect.stack()
        file_line = 'Unknown file and line'

        app_patterns = ['accounts',]

        for frame in stack:
            for pattern in app_patterns:
                if pattern in frame.filename and frame.filename.endswith('.py'):
                    file_line = f'{frame.filename}:{frame.lineno}'
                    break

            if file_line != 'Unknown file and line':
                break

        else:
            caller_frame = stack[-1]
            file_line = f'{caller_frame.filename}:{caller_frame.lineno}'

        record.file_line = file_line

        return super().format(record)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'rich.logging.RichHandler',
            'formatter': 'custom',
            'filters': ['exception_only'],
            'rich_tracebacks': True,
        },
        'debug_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/debug.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'formatter': 'custom',
            'filters': ['exception_only'],
            'backupCount': 2,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
        },
        'system_log_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/djangologs.log',
            'mode': 'a',
            'encoding': 'utf-8',
            'formatter': 'custom',
            'filters': ['exception_only'],
            'backupCount': 2,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
        },
        "celery_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/logs/celery.log",
            "mode": "a",
            "encoding": "utf-8",
            "formatter": "custom",
            "backupCount": 2,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
        "gunicorn_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": f"{BASE_DIR}/logs/gunicorn_access.log",
            "mode": "a",
            "encoding": "utf-8",
            "formatter": "custom",
            "backupCount": 2,
            "maxBytes": 1024 * 1024 * 5,  # 5 MB
        },
    },
    'filters': {
        'exception_only': {
            '()': ExceptionFilter,
        },
    },
    'formatters': {
        'custom': {
            '()': CustomFormatter,
            'format': '{levelname} - {asctime} // {name} | {funcName} || {file_line}: {message}',
            'style': '{',
        },
    },
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console', 'system_log_handler'],
            'propagate': False,
        },
        'celery': {
            'level': LOG_LEVEL,
            'handlers': ['console', 'celery_handler'],
            'propagate': False,
        },
        'gunicorn': {
            'level': LOG_LEVEL,
            'handlers': ['gunicorn_handler'],
            'propagate': False,
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console',],
    }
}


logging.config.dictConfig(LOGGING)
