import os
import sys

class PassengerPathInfoFix(object):
    """
    Sets PATH_INFO from REQUEST_URI since Passenger doesn't provide it.
    """
    def init(self, app):
        self.app = app

    def call(self, environ, start_response):
        from urllib.parse import unquote
        environ['SCRIPT_NAME'] = ''

        request_uri = unquote(environ['REQUEST_URI'])
        script_name = unquote(environ.get('SCRIPT_NAME', ''))
        offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
        environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
        return self.app(environ, start_response)


# Replace projectname with the name of the main folder containing wsgi.py and setting.py
import Incident.Incident.wsgi
application = Incident.Incident.wsgi.application
application = PassengerPathInfoFix(application)