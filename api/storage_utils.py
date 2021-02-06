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
    try:
        blob.upload_from_filename(file)
        return 0
    except:
        print("File {} was not found".format(file))
        return 1

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
    try:
        blob.download_to_filename(filename)
        return 0
    except:
        print("File {} was not found".format(filename))
        return 1

"""
    Delete a file from GCP storage
    Args:
        String - File name
    Returns:
        None
"""
def delete(filename):
    project_name = "capstone-90db7"
    bucket_name = 'capstone-90db7.appspot.com'

    storage_client = storage.Client(project=project_name)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.delete()
