import dash
import dash.html as html
import dash.dcc as dcc
from dash.dependencies import Input, Output, State
from app import app

# Define the layout of the login page
login_layout = html.Div(id='login-content',
                        children=[
                            html.H2("Login"),
                            html.Div([
                                html.Label('Username'),
                                dcc.Input(id='username', type='text')
                            ]),
                            html.Div([
                                html.Label('Password'),
                                dcc.Input(id='password', type='password')
                            ]),
                            html.Button('Login', id='login-button'),
                            html.Div(id='login-error')
                        ],
                        style={
                            'marginLeft': '250px'
                        }
                )


# Define a callback to handle page navigation
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/login':
        return login_layout
    else:
        return "Error"


# Define a callback to handle page navigation
# @callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/login':
#         return login_layout
#     else:
#         return landing_page_layout


