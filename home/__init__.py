"""
 the home app represents the main appplication for the domain
 it can be reached as example.com, www.example.com, or home.example.com 
 These subdomains are all hard-coded in the dispatcher.
 I know that's not good, see the comments in the dispatcher...
"""

import logging 
logger = logging.getLogger(__name__)

from flask import Flask 

subdomain = 'home'

def create_app(config=None):
    domain = None 
    if config:
        domain = config.get('domain')

    logger.info(f'creating app for {subdomain}.{domain}')
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/')
    def index():
        logger.info(f'in {subdomain}:index')
        return f'Hello from the home of {domain}!'

    return app 


## end of file 