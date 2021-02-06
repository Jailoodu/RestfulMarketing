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
    GET /marketing/
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/files/download', json={"file":"p1.rb"})
        assert response.status_code == 200
        assert response.status == "200 OK"
        assert path.exists("p1.rb")
        
        if path.exists("p1.rb"):
            os.remove("p1.rb")

def test_download_fail():
    """
    GET /marketing/
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/api/files/download', json={"file":"nothing.txt"})
        assert response.status_code == 400
        assert response.status == "400 BAD REQUEST"
        os.remove("nothing.txt")
        
def test_upload():
    """
    POST /marketing/
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/files/upload', json={"file":".gitignore"})
        assert response.status_code == 201
        delete(".gitignore")

def test_upload_fail():
    """
    POST /marketing/
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.post('/api/files/upload', json={"file":"hello.txt"})
        assert response.status_code == 400
        assert response.status == "400 BAD REQUEST"