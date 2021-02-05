from google.cloud import storage
import ntpath

"""
    Upload a file to GCP storage
    Args:
        String - Path to file
    Returns:
        None
"""
def upload(file):
    project_name = "capstone-90db7"
    bucket_name = 'capstone-90db7.appspot.com'

    client = storage.Client(project=project_name)
    bucket = client.get_bucket(bucket_name)
    filename = ntpath.basename(file)
    blob = bucket.blob(filename)
    blob.upload_from_filename(file)

"""
    Download a file from GCP storage
    Args:
        String - File name
    Returns:
        None
"""
def download(filename):
    project_name = "capstone-90db7"
    bucket_name = 'capstone-90db7.appspot.com'

    storage_client = storage.Client(project=project_name)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.download_to_filename(filename)
