from dash import html
import dash_bootstrap_components as dbc


def home_layout():

    return dbc.Container(

        [
            html.H2("Data Explorer Dashboard"),

            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4("Total Datasets"),
                            html.H2(id="total-datasets")
                        ])
                    ),
                    width=4
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4("Total Rows"),
                            html.H2(id="total-rows")
                        ])
                    ),
                    width=4
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4("Storage Used"),
                            html.H2(id="storage-used")
                        ])
                    ),
                    width=4
                )
            ]),

            html.Br(),

            dbc.Card(
                dbc.CardBody([
                    html.H4("Recent Datasets"),
                    html.Div(id="recent-datasets-table")
                ])
            )

        ],
        fluid=True
    )