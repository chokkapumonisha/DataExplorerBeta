from dash import Input, Output, State
from app import app
import plotly.express as px
from services.api import request_visualization


@app.callback(

    Output("main-chart", "figure"),

    Input("generate-chart", "n_clicks"),

    State("viz-dataset-dropdown", "value"),
    State("chart-type", "value"),
    State("x-axis", "value"),
    State("y-axis", "value")

)
def generate_chart(n, dataset, chart_type, x, y):

    if n is None:
        return {}

    payload = {

        "dataset": dataset,
        "chart_type": chart_type,
        "x": x,
        "y": y

    }

    data = request_visualization(payload)

    df = data["dataframe"]

    if chart_type == "scatter":
        fig = px.scatter(df, x=x, y=y)

    elif chart_type == "bar":
        fig = px.bar(df, x=x, y=y)

    elif chart_type == "histogram":
        fig = px.histogram(df, x=x)

    else:
        fig = px.box(df, x=x, y=y)

    return fig