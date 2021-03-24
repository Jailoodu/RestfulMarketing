from api.storage_utils import upload, download, delete, email
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

def send_email(data):
    recipient_list = data["to"]
    subject = data["subject"]
    text = data["text"]
    res = email(recipient_list, subject, text) 
    if res.status_code == 200:
        return 0
    return 1
    