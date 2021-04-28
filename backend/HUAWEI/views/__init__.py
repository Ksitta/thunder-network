from apscheduler.schedulers.background import BackgroundScheduler
from .task import flow_info

scheduler = BackgroundScheduler()
scheduler.add_job(flow_info, 'interval', seconds=60)
with open('./log.txt', mode='a+') as file:
    file.write("successfully added task\n")
print("successfully added task\n")
scheduler.start()
