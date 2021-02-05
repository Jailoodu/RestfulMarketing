from api.storage_utils import upload, download

"""
    Upload a file to GCP storage
    Args:
        String - Path to file
    Returns:
        None
"""
def upload_file(data):
    file = data["file"]
    upload(file)

def download_file(data):
    file = data["file"]
    download(file)