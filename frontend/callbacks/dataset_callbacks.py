from dash import Input, Output
from app import app
from services.api import get_datasets


@app.callback(

    Output("dataset-table", "data"),
    Output("dataset-table", "columns"),

    Input("url", "pathname")

)
def load_datasets(_):

    datasets = get_datasets()

    if not datasets:
        return [], []

    columns = [{"name": k, "id": k} for k in datasets[0].keys()]

    return datasets, columns