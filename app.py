import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, Blueprint
from api.api import api 
from api.endpoints.marketing import namespace as ns 

# initialize a Flash (WSGI) application
app = Flask(__name__)

def start_app(app):
    # the endpoint will be hostname:port/api
    bp = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(bp)
    api.add_namespace(ns)
    # blueprint helps organize a group of related views
    app.register_blueprint(bp)

def main():
    start_app(app)
    app.run(host ='127.0.0.1', port = 5000)

# main function is automatically run
if __name__ == '__main__':
    main()