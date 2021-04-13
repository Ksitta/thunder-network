from threading import Timer
import time
from .flow_generate_view import FlowGenerateView

generator = FlowGenerateView()


def get_flow():
    global t
    logfile = open('./flow.log', mode='w+')
    logfile.write(str(time.time()) + " generated a flow message")
    logfile.close()
    generator.inner_generate()
    t = Timer(14400, get_flow)
    t.start()


t = Timer(14400, get_flow)
t.start()