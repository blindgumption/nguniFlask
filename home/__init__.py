"""
 the home app represents the base of blindgumption.
 it can be reached as blindgumption.com, www.blindgumption.com, or home.blindgumption.com 
"""

# first get logger to ensure root logger is set before anything is initiated 
from jsonloggeriso8601datetime import getJsonLogger 
logger = getJsonLogger(__name__)

from flask import Flask 

def create_app(config_name=None):
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/')
    def index():
        logger.info('in home:index')
        return 'Hello from the home of BlindGumption!'

    return app 


