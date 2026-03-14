from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session

from database import get_db
from dataset_manager import DatasetManager
from analytics_engine import AnalyticsEngine
from data_cleaning import DataCleaning
from models.dataset import Dataset

app = FastAPI()

dataset_manager = DatasetManager()


@app.post("/upload_dataset")
def upload_dataset(file: UploadFile = File(...), db: Session = Depends(get_db)):

    dataset = dataset_manager.upload_dataset(file, db)

    return {"dataset_id": dataset.id}


@app.get("/datasets")
def list_datasets(db: Session = Depends(get_db)):

    datasets = db.query(Dataset).all()

    return datasets


@app.get("/dataset/{dataset_id}")
def get_dataset(dataset_id: int, db: Session = Depends(get_db)):

    df = dataset_manager.load_dataset(dataset_id, db)

    return df.head(20).to_dict()


@app.post("/clean_dataset/{dataset_id}")
def clean_dataset(dataset_id: int, db: Session = Depends(get_db)):

    df = dataset_manager.load_dataset(dataset_id, db)

    df = DataCleaning.clean_dataframe(df)

    return {"rows_after_cleaning": df.shape[0]}


@app.get("/dataset_summary/{dataset_id}")
def dataset_summary(dataset_id: int, db: Session = Depends(get_db)):

    df = dataset_manager.load_dataset(dataset_id, db)

    summary = AnalyticsEngine.dataset_summary(df)

    return summary


@app.get("/visualization_data/{dataset_id}")
def visualization_data(dataset_id: int, db: Session = Depends(get_db)):

    df = dataset_manager.load_dataset(dataset_id, db)

    corr = AnalyticsEngine.correlation_matrix(df)

    return corr