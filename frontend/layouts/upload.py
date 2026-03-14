from dash import html, dcc
import dash_bootstrap_components as dbc


def upload_layout():

    return dbc.Container(

        [
            html.H2("Upload Dataset"),

            dbc.Card(
                dbc.CardBody([

                    dcc.Upload(
                        id="dataset-upload",
                        children=html.Div([
                            "Drag and Drop or ",
                            html.A("Select CSV File")
                        ]),
                        style={
                            "width": "100%",
                            "height": "120px",
                            "lineHeight": "120px",
                            "borderWidth": "2px",
                            "borderStyle": "dashed",
                            "borderRadius": "5px",
                            "textAlign": "center",
                        },
                        multiple=False
                    ),

                    html.Br(),

                    dbc.Button(
                        "Upload",
                        id="upload-button",
                        color="primary"
                    ),

                    html.Div(id="upload-status")

                ])
            )
        ],
        fluid=True
    )