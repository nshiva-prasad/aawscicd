from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.signals import setup_logging
from logging.config import dictConfig
from django.conf import settings  



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joyfulsurprises.settings')


celery_app = Celery('joyfulsurprises')

celery_app.conf.broker_connection_retry_on_startup = True


celery_app.config_from_object('django.conf:settings', namespace='CELERY')

@setup_logging.connect
def config_loggers(*args, **kwargs):
    dictConfig(settings.LOGGING)


celery_app.autodiscover_tasks()

