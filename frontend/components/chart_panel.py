from dash import dcc, html


def chart_panel(graph_id):

    return html.Div(

        dcc.Loading(
            dcc.Graph(id=graph_id),
            type="circle"
        ),

        className="chart-panel"
    )