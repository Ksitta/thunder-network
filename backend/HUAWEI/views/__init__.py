from apscheduler.schedulers.background import BackgroundScheduler
from .flow_generate_view import FlowGenerateView

a = FlowGenerateView()

scheduler = BackgroundScheduler()
scheduler.add_job(a.inner_generate, 'interval', seconds=60)
scheduler.start()
