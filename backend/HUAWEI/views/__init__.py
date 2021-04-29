from apscheduler.schedulers.background import BackgroundScheduler
from .flow_generate_view import FlowGenerateView
try:
    from config.local_settings import interval_time
except:
    interval_time = 3600

a = FlowGenerateView()

scheduler = BackgroundScheduler()
scheduler.add_job(a.inner_generate, 'interval', seconds=interval_time)
scheduler.start()
