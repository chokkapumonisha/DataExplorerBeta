from dash import dcc

def loading_graph(graph_id):

    return dcc.Loading(
        children=dcc.Graph(id=graph_id),
        type="circle"
    )