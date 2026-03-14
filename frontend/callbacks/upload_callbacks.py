import base64
from dash import Input, Output, State
from app import app
from services.api import upload_dataset


@app.callback(

    Output("upload-status", "children"),

    Input("upload-button", "n_clicks"),

    State("dataset-upload", "contents"),
    State("dataset-upload", "filename")

)
def upload_file(n, contents, filename):

    if n is None or contents is None:
        return ""

    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)

    response = upload_dataset(decoded, filename)

    return f"Upload successful: {response}"