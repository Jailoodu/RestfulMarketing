from api.api import api
from flask_restplus import Resource
from flask import request, jsonify, make_response, Response
from werkzeug.utils import secure_filename
from api.implementation import upload_file, download_file

# namespace sets the endpoints with a prefix of /users
namespace = api.namespace('files', description='Operations on marketing resources')

@namespace.route('/upload') 
class MarketingCollectionUpload(Resource):
    @api.doc(responses = {201: 'File uploaded', 400: 'Error occurred' })
    def post(self):
        """
        Upload file
        """
        if request.is_json and request.json["file"]:
            rc = upload_file(request.json)
            if rc == 1:
                return None, 400
            else:
                return None, 201
        return None, 400

@namespace.route('/download')
class MarketingCollectionDownload(Resource):
    @api.doc(responses = {200: 'File fetched', 400: 'Error occurred' })
    def get(self):
        """
        Download file
        """
        rc = download_file(request.json)
        if rc == 1:
            return None, 400
        return None, 200

