import pytest
from flask import json
from app import app, start_app
import os.path
from os import path
from api.storage_utils import delete 

flask_app = app
start_app(flask_app)

def test_download():
    """
    GET /api/files/download
    Requirements: F-34
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/files/download', json={"file":"data.json"})
        assert response.status_code == 200
        assert response.status == "200 OK"
        assert path.exists("data.json")
        
        if path.exists("data.json"):
            os.remove("data.json")

def test_download_negative():
    """
    GET /api/files/download
    Requirements: F-34
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/files/download', json={"file":"nothing.txt"})
        assert response.status_code == 400
        assert response.status == "400 BAD REQUEST"
        os.remove("nothing.txt")
        
def test_upload():
    """
    POST /api/files/upload
    Requirements: F-34
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/files/upload', json={"file":".gitignore"})
        assert response.status_code == 201
        delete(".gitignore")

def test_upload_negative():
    """
    POST /api/files/upload
    Requirements: F-34
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/files/upload', json={"file":"hello.txt"})
        assert response.status_code == 400
        assert response.status == "400 BAD REQUEST"

def test_delete_file_fail():
    """
    DELETE /api/files/delete
    Requirements: F-34
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/files/upload', json={"file":".gitignore"})
        assert response.status_code == 201
        response = test_client.delete('/api/files/delete', json={"file":".gitignore"})
        assert response.status_code == 204
        assert response.status == "204 NO CONTENT"

def test_edit_fail():
    """
    PUT /api/marketing/edit
    Requirements: F-34
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.put('/api/marketing/edit', json={"file":"img.jpg"})
        assert response.status_code == 204
        assert response.status == "204 No Content"

# Due to limitations of the Mailgun API, this test has been excluded for now
# def test_send_email():
#     """
#     POST /api/share/email
#     """
#     # A test client configured for testing
#     with flask_app.test_client() as test_client:
#         response = test_client.post('/api/share/email', json={"to":"jason.loodu@gmail.com", "subject": "Test email", "text":"Example message"})
#         assert response.status_code == 200
#         assert response.status == "200 OK"