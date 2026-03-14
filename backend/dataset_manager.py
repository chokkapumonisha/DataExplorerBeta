import pandas as pd
from sqlalchemy.orm import Session
from models.dataset import Dataset
from blob_storage import BlobStorage
from utils.logger import get_logger
from io import BytesIO

logger = get_logger("dataset_manager")

class DatasetManager:

    def __init__(self):

        self.storage = BlobStorage()

    def upload_dataset(self, file, db: Session):

        try:

            content = file.file.read()

            df = pd.read_csv(BytesIO(content))

            blob_name = file.filename

            self.storage.upload_file(blob_name, content)

            dataset = Dataset(
                name=file.filename,
                blob_path=blob_name,
                rows=df.shape[0],
                columns=df.shape[1]
            )

            db.add(dataset)
            db.commit()
            db.refresh(dataset)

            logger.info(f"Dataset stored: {dataset.id}")

            return dataset

        except Exception as e:

            logger.error(f"Upload failed: {e}")
            raise

    def load_dataset(self, dataset_id: int, db: Session):

        dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()

        if not dataset:
            raise Exception("Dataset not found")

        blob_data = self.storage.download_file(dataset.blob_path)

        df = pd.read_csv(BytesIO(blob_data))

        return df