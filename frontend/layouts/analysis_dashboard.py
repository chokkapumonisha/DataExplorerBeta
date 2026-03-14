from dash import html, dcc
import dash_bootstrap_components as dbc


def analysis_layout():

    return dbc.Container(

        [

            html.H2("Analysis Dashboard"),

            dbc.Row(

                [

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Mean"),
                                    html.H3(id="mean-value")
                                ]
                            )
                        ),
                        width=3
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Median"),
                                    html.H3(id="median-value")
                                ]
                            )
                        ),
                        width=3
                    ),

                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Std Dev"),
                                    html.H3(id="std-value")
                                ]
                            )
                        ),
                        width=3
                    )

                ]

            ),

            html.Br(),

            dcc.Graph(id="correlation-heatmap")

        ],

        fluid=True
    )