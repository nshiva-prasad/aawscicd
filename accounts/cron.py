# # joyfulsurprises/accounts/cron.py

import logging
from django_cron import CronJobBase, Schedule
from .models import CustomUser

logger = logging.getLogger(__name__)

class GoogleIntegrationsCronJob(CronJobBase):
    RUN_EVERY_MINUTES = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINUTES)
    code = 'apps.integrations.google_sheet_changes'  # a unique code

    def do(self):
        logger.info(f"Running Cron Job {self.code}")

        print("Fetching emails from CustomUser model...")
        emails = CustomUser.objects.values_list('email', flat=True)
        for email in emails:
            print(email)
        logger.info("Fetched and printed all emails from CustomUser model.")


def task_function():
    print("Fetching emails from CustomUser model...")
    emails = CustomUser.objects.values_list('email', flat=True)
    for email in emails:
        print(email)
    print("Fetched and printed all emails from CustomUser model.")