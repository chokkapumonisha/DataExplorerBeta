import requests
from config import API_BASE_URL


def get_datasets():
    r = requests.get(f"{API_BASE_URL}/datasets")
    return r.json()


def upload_dataset(file_content, filename):

    files = {
        "file": (filename, file_content)
    }

    r = requests.post(f"{API_BASE_URL}/upload", files=files)

    return r.json()


def delete_dataset(dataset_id):

    r = requests.delete(f"{API_BASE_URL}/dataset/{dataset_id}")

    return r.json()


def get_dataset_metadata(dataset_id):

    r = requests.get(f"{API_BASE_URL}/dataset/{dataset_id}")

    return r.json()


def request_visualization(payload):

    r = requests.post(f"{API_BASE_URL}/visualization", json=payload)

    return r.json()


def get_reports():

    r = requests.get(f"{API_BASE_URL}/reports")

    return r.json()