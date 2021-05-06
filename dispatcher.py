""" 
the dispatcher is middleware used by gunicorn to route requests to subdomains of blindgumption.com

This idea is from the flask documentation, see:
    https://flask.palletsprojects.com/en/1.1.x/patterns/appdispatch/#app-dispatch
"""

# first get logger to ensure root logger is set before anything is initiated 
from jsonloggeriso8601datetime import getJsonLogger 
logger = getJsonLogger(__name__)


from threading import Lock

dispatcher_count = 0 

class SubdomainDispatcher(object):

    def __init__(self, domain, create_app):
        logger.info(f'creating dispatcher for domain {domain}')
        self.domain = domain
        self.create_app = create_app
        self.lock = Lock()
        self.instances = {}

    def get_application(self, host):
        host = host.split(':')[0]
        assert host.endswith(self.domain), 'Configuration error'
        subdomain = host[:-len(self.domain)].rstrip('.')
        if subdomain in [None, '', 'home', 'www']:
            # domain details leaking into middleware??? 
            subdomain = 'home'
        with self.lock:
            # with instances being an object instance variable,
            # do we really need this lock?
            # each worker has its own instance of the dispatcher application 
            # maybe the lock is needed if using this dispatcher in something other than gunicorn, 
            # or a different configuration for gunicorn.   
            app = self.instances.get(subdomain)
            if app is None:
                logger.info(f"adding app for subdomain [{subdomain}], instances has [{len(self.instances)}] apps")
                app = self.create_app(subdomain, self.domain)
                self.instances[subdomain] = app
                logger.debug(f"added app [{app}] for subdomain [{subdomain}], instances now has [{len(self.instances)}] apps")
            return app

    def __call__(self, environ, start_response):
        app = self.get_application(environ['HTTP_HOST'])
        return app(environ, start_response)

## This dispatcher can then be used like this:
import home 
import blog 
from werkzeug.exceptions import NotFound

def make_app(subdomain, domain):
    logger.info(f'making app for subdomain {subdomain}')
    config = {'domain': domain, 'subdomain': subdomain}
    try:
        if subdomain == 'home':
            return home.create_app(config)
        elif subdomain == 'blog':
            return blog.create_app(config)
        else:  
            # if there is no app for that subdomain we still have
            # to return a WSGI application that handles that request.
            # We can then just return the NotFound() exception as
            # application which will render a default 404 page.
            # You might also redirect the user to the main page then
            return NotFound()
    except Exception as e:
        logger.exception('exception when trying to create new application')

application  = SubdomainDispatcher('ngunif.local', make_app)
