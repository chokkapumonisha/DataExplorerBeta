import dash_bootstrap_components as dbc
from dash import html


def create_navbar():

    return dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("Data Explorer", href="/"),

                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/"),
                        dbc.NavLink("Upload", href="/upload"),
                        dbc.NavLink("Datasets", href="/datasets"),
                        dbc.NavLink("Analysis", href="/analysis"),
                        dbc.NavLink("Visualization", href="/visualization"),
                        dbc.NavLink("Reports", href="/reports"),
                    ],
                    pills=True
                )
            ]
        ),
        color="dark",
        dark=True
    )