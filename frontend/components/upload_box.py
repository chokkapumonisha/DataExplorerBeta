from dash import dcc, html


def upload_box():

    return dcc.Upload(

        id="dataset-upload",

        children=html.Div([
            "Drag & Drop or ",
            html.A("Select CSV File")
        ]),

        className="upload-box",

        multiple=False
    )