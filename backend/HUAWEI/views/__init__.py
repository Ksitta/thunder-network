# from threading import Timer
# import time
# from .flow_generate_view import FlowGenerateView
# try:
#     from config.local_settings import deploy
# except:
#     deploy = False
#
# generator = FlowGenerateView()
#
# global t
#
# def get_flow():
#     global t
#     logfile = open('./flow.log', mode='a+')
#     logfile.write(str(time.time()) + " generated a flow message")
#     logfile.close()
#     generator.inner_generate()
#     t = Timer(14400, get_flow)
#     t.start()
#
# if deploy:
#     t = Timer(10, get_flow)
#     t.start()
