from dash import html
import dash_bootstrap_components as dbc


def create_sidebar():

    return html.Div(

        [
            html.H4("Navigation", className="text-light"),

            html.Hr(),

            dbc.Nav(
                [

                    dbc.NavLink("Dashboard", href="/"),
                    dbc.NavLink("Upload Dataset", href="/upload"),
                    dbc.NavLink("Dataset Manager", href="/datasets"),
                    dbc.NavLink("Analysis", href="/analysis"),
                    dbc.NavLink("Visualization", href="/visualization"),
                    dbc.NavLink("Reports", href="/reports")

                ],
                vertical=True,
                pills=True
            )
        ],

        className="sidebar"
    )