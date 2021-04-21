""" 
see https://docs.gunicorn.org/en/stable/settings.html#settings 
to understand the values below 
"""


import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
## workers = 1

bind = "127.0.0.1:8000"
wsgi_app = "dispatcher:application"  
errorlog = "./gunicorn.error.log"
loglevel = "debug"
capture_output = True 
