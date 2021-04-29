from apscheduler.schedulers.background import BackgroundScheduler
from .flow_generate_view import FlowGenerateView
try:
    from config.local_settings import interval_time
except:
    interval_time = 3600


def generate_flow():
    a = FlowGenerateView()
    a.inner_generate()


scheduler = BackgroundScheduler()
scheduler.add_job(generate_flow, 'interval', seconds=interval_time)
scheduler.start()
