from azure.storage.blob import BlobServiceClient
from config import Config
from utils.logger import get_logger

logger = get_logger("blob_storage")

class BlobStorage:

    def __init__(self):

        self.client = BlobServiceClient.from_connection_string(
            Config.AZURE_CONNECTION_STRING
        )

        self.container = self.client.get_container_client(
            Config.AZURE_CONTAINER_NAME
        )

    def upload_file(self, file_name: str, data: bytes):

        blob_client = self.container.get_blob_client(file_name)

        blob_client.upload_blob(data, overwrite=True)

        logger.info(f"Uploaded file {file_name}")

        return file_name

    def download_file(self, blob_name: str):

        blob_client = self.container.get_blob_client(blob_name)

        data = blob_client.download_blob().readall()

        logger.info(f"Downloaded file {blob_name}")

        return data