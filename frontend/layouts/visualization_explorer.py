from dash import html, dcc
import dash_bootstrap_components as dbc


def visualization_layout():

    return dbc.Container([

        html.H2("Visualization Explorer"),

        dbc.Row([

            dbc.Col([

                html.Label("Select Dataset"),
                dcc.Dropdown(id="viz-dataset-dropdown"),

                html.Label("Chart Type"),
                dcc.Dropdown(
                    id="chart-type",
                    options=[
                        {"label": "Scatter", "value": "scatter"},
                        {"label": "Bar", "value": "bar"},
                        {"label": "Histogram", "value": "histogram"},
                        {"label": "Box", "value": "box"}
                    ]
                ),

                html.Label("X Axis"),
                dcc.Dropdown(id="x-axis"),

                html.Label("Y Axis"),
                dcc.Dropdown(id="y-axis"),

                dbc.Button("Generate Chart", id="generate-chart")

            ], width=3),

            dbc.Col([

                dcc.Loading(
                    dcc.Graph(id="main-chart"),
                    type="circle"
                )

            ], width=9)

        ])

    ], fluid=True)