import dash
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from component.sidebar import sidebar
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# Define the layout of the landing page
landing_page_layout = html.Div(
    children=[
        html.H1(
            children="Hello World - Landing Page",
            className="header"
        ),
        dcc.Link('Go to Second Page', href='/login')
    ],
    style={
                'marginLeft': '220px'
    }
)

# Define the layout of the second page
second_page_layout = html.Div(
    children=[
        html.H1(
            children="Hello World - Second Page",
            className="header"
        ),
        dcc.Link('Go back to Landing Page', href='/')
    ],
    style={
            'marginLeft': '220px'
    }
)

# Define the main layout that includes a location component for page navigation
app.layout = html.Div(
    children=[
        sidebar,
        html.Div(
            children=[
                dcc.Location(id='url', refresh=False),
                html.Div(id='page-content')
            ]
        )
    ]
)

# Define a callback to handle page navigation
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return second_page_layout
    else:
        return landing_page_layout

if __name__ == '__main__':
    app.run_server(debug=True)
