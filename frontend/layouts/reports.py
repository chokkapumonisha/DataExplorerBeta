from dash import html
import dash_bootstrap_components as dbc
from dash import dash_table


def reports_layout():

    return dbc.Container(

        [

            html.H2("Reports"),

            dbc.Card(

                dbc.CardBody(

                    [

                        dash_table.DataTable(

                            id="reports-table",

                            page_size=10,

                            style_table={"overflowX": "auto"}

                        ),

                        html.Br(),

                        dbc.Button(
                            "Download Report",
                            id="download-report",
                            color="primary"
                        )

                    ]

                )

            )

        ],

        fluid=True
    )