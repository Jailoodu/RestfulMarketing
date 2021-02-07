import pytest
from flask import json
from app import app, start_app
import os.path
from os import path
from api.storage_utils import delete
from tests.test_app import flask_app

def test_download_stress():
    """
    GET /api/files/download
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        for i in range(10):
            print("Fetching file from Firestore, iteration #{}".format(i))
            response = test_client.get('/api/files/download', json={"file":"data.json"})
            assert response.status_code == 200
            assert response.status == "200 OK"
            assert path.exists("data.json")
            
            if path.exists("data.json"):
                os.remove("data.json")

def test_upload_stress():
    """
    POST /api/files/upload
    """
    # A test client configured for testing
    with flask_app.test_client() as test_client:
        for i in range(10):
            print("Uploading file to Firestore, iteration #{}".format(i))
            response = test_client.post('/api/files/upload', json={"file":".gitignore"})
            assert response.status_code == 201
            delete(".gitignore")