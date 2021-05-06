""" 
see https://docs.gunicorn.org/en/stable/settings.html#settings 
to understand the values below 
"""

from jsonloggeriso8601datetime.jsonloggerdictconfig import dictConfig 

import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
## workers = 1

bind = "127.0.0.1:8000"
wsgi_app = "dispatcher:application"  
accesslog = "./logs/gunicorn.access.log"
errorlog = "./logs/gunicorn.error.log"
loglevel = "info"
logconfig_dict = dictConfig 
capture_output = True 
