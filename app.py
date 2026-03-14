import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from components.navbar import create_navbar
from layouts.home import home_layout
from layouts.upload import upload_layout
from layouts.dataset_manager import dataset_manager_layout
from layouts.analysis_dashboard import analysis_layout
from layouts.visualization_explorer import visualization_layout
from layouts.reports import reports_layout

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server

app.layout = html.Div([
    dcc.Location(id="url"),
    create_navbar(),
    html.Div(id="page-content")
])


def display_page(pathname):

    routes = {
        "/": home_layout(),
        "/upload": upload_layout(),
        "/datasets": dataset_manager_layout(),
        "/analysis": analysis_layout(),
        "/visualization": visualization_layout(),
        "/reports": reports_layout()
    }

    return routes.get(pathname, home_layout())


@app.callback(
    dash.Output("page-content", "children"),
    dash.Input("url", "pathname")
)
def render_page(pathname):
    return display_page(pathname)


if __name__ == "__main__":
    app.run(debug=True)