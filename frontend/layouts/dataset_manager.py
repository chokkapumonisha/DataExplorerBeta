from dash import html
import dash_bootstrap_components as dbc
from dash import dash_table


def dataset_manager_layout():

    return dbc.Container(

        [
            html.H2("Dataset Manager"),

            dbc.Card(
                dbc.CardBody([

                    dash_table.DataTable(
                        id="dataset-table",
                        page_size=10,
                        style_table={"overflowX": "auto"},
                        style_cell={"textAlign": "left"},
                        row_selectable="single"
                    ),

                    html.Br(),

                    dbc.Button("Delete Dataset", id="delete-dataset", color="danger"),
                    dbc.Button("View Metadata", id="view-metadata", color="info")

                ])
            )

        ],
        fluid=True
    )