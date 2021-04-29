from apscheduler.schedulers.background import BackgroundScheduler
from .cron import flow_info, test_con

scheduler = BackgroundScheduler()
scheduler.add_job(flow_info, 'interval', seconds=3600)

scheduler.add_job(test_con, 'interval', seconds=60)
scheduler.start()
