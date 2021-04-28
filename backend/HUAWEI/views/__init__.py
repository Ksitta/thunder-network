from apscheduler.schedulers.background import BackgroundScheduler
from .task import flow_info

scheduler = BackgroundScheduler()
scheduler.add_job(flow_info, 'interval', seconds=60)
scheduler.start()
