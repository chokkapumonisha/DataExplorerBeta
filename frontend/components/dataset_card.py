from dash import html
import dash_bootstrap_components as dbc


def dataset_card(name, rows, columns):

    return dbc.Card(

        dbc.CardBody(

            [

                html.H5(name),

                html.P(f"Rows: {rows}"),
                html.P(f"Columns: {columns}")

            ]

        ),

        className="dataset-card"
    )