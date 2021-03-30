"""
Command to load general test data
"""
import os

from django.core.management.base import BaseCommand
from django.db import transaction

from tests.data_generate_test import GenerateTool as Tool

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('begin handle')
        with transaction.atomic():
            os.system('python manage.py loaddata admin')
            t = Tool()
            t.generate_data()
        print('end handle')
