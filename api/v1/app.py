#!/usr/bin/python3

'''
create flask app and register the blueprint app_views to Flask instance app
'''

from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r"/app/v1/*": {"origins": "0.0.0.0"}})

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_engine(exception):
    '''

    '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    '''

    '''

    response = {"error": "Not found"}
    return jsonify(response), 404


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(debug=True, host=HOST, port=PORT, threaded=True)
