from api.api import api
from flask_restplus import Resource, fields
from flask import request, jsonify, make_response, Response
from werkzeug.utils import secure_filename
from api.implementation import upload_file, download_file, delete_file, send_email
import sys

# namespace sets the endpoints with a prefix of /users
namespace = api.namespace('files', description='Operations on marketing resources')

# Model for file operations
file_model = namespace.model(
    "File",
    {
        "file": fields.String(description="File name", required=True)
    },
)

@namespace.route('/upload') 
class MarketingCollectionUpload(Resource):
    @api.doc(responses = {201: 'File uploaded', 400: 'Error occurred' })
    @namespace.expect(file_model)
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
    @namespace.expect(file_model)
    def get(self):
        """
        Download file
        """
        rc = download_file(request.json)
        if rc == 1:
            return None, 400
        return None, 200

@namespace.route('/delete')
class MarketingCollectionDelete(Resource):
    @api.doc(responses = {204: 'File deleted', 400: 'Error occurred'})
    @namespace.expect(file_model)
    def delete(self):
        """
        Delete file
        """
        delete_file(request.json)
        return None, 204

# namespace sets the endpoints with a prefix of /share
marketingnamespace = api.namespace('share', description='Operations involving sharing resources')

# Model for sending emails
email_model = marketingnamespace.model(
    "Email",
    {
        "to": fields.String(description="Recipient of email", required=True),
        "subject": fields.String(description="Subject of email", required=True),
        "text": fields.String(description="Email text", required=True),
    },
)

@marketingnamespace.route('/email') 
class MarketingCollectionEmail(Resource):
    @api.doc(responses = {200: 'Email sent', 400: 'Error occurred' })
    @marketingnamespace.expect(email_model)
    def post(self):
        """
        Send an email
        """
        rc = send_email(request.json)
        if rc == 1:
            return None, 400
        return None, 200
