from dash import Input, Output
from app import app
import plotly.express as px
import pandas as pd
from services.api import get_dataset_metadata


@app.callback(

    Output("mean-value", "children"),
    Output("median-value", "children"),
    Output("std-value", "children"),

    Input("viz-dataset-dropdown", "value")

)
def update_stats(dataset_id):

    if dataset_id is None:
        return "-", "-", "-"

    data = get_dataset_metadata(dataset_id)

    df = pd.DataFrame(data["data"])

    mean = round(df.mean().mean(), 2)
    median = round(df.median().median(), 2)
    std = round(df.std().mean(), 2)

    return mean, median, std