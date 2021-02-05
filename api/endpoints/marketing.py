from api.api import api
from flask_restplus import Resource
from flask import request, jsonify, make_response, Response
from werkzeug.utils import secure_filename
from api.implementation import upload_file, download_file

# namespace sets the endpoints with a prefix of /users
namespace = api.namespace('marketing', description='Operations on marketing resources')

@namespace.route('/') 
class MarketingCollection(Resource):
    @api.doc(responses = {201: 'File uploaded', 400: 'Error occurred' })
    def post(self):
        """
        Upload file
        """
        if request.is_json and request.json["file"]:
            upload_file(request.json)
            return None, 201
        return None, 400

    @api.doc(responses = {200: 'File fetched', 400: 'Error occurred' })
    def get(self):
        """
        Download file
        """
        if request.is_json and request.json["file"]:
            download_file(request.json)
            return None, 200
        return None, 400

