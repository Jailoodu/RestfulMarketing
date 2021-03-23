from api.storage_utils import upload, download, delete
import os.path
from os import path

"""
    Upload a file to GCP storage
    Args:
        String - Path to file
    Returns:
        None
"""
def upload_file(data):
    file = data["file"]
    if not path.exists(file):
        return 1
    return upload(file)

def download_file(data):
    file = data["file"]
    return download(file)

def delete_file(data):
    file = data["file"]
    return delete(file)
    