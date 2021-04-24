from apscheduler.schedulers.background import BackgroundScheduler
from django.test.client import Client
from django.urls import reverse


def generate_flow():
    a = Client()
    a.get(reverse('flow_generate'))


scheduler = BackgroundScheduler()
scheduler.add_job(generate_flow, 'interval', seconds=3600)
scheduler.start()
