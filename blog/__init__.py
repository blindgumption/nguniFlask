"""
 the blog app is the first application on blindgumption
 it can be reached as blog.blindgumption.com
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
        logger.info('in blog:index')
        return 'Hello from the BlindGumption blog!  Blog on Wayne!!  Blog on Garth!!'

    return app 


