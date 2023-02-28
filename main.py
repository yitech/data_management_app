import dash
import dash.html as html
import dash.dcc as dcc
from dash.dependencies import Input, Output, State


# Define external CSS stylesheets
external_stylesheets = [
    'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css',
    'https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H2("Login Page"),
    dcc.Input(id='username', type='text', placeholder='Username'),
    dcc.Input(id='password', type='password', placeholder='Password'),
    html.Button('Login', id='login-button', n_clicks=0),
    html.Div(id='output-state')
])

@app.callback(Output('output-state', 'children'),
              Input('login-button', 'n_clicks'),
              State('username', 'value'),
              State('password', 'value'))
def authenticate_user(n_clicks, username, password):
    if n_clicks > 0:
        if username == 'admin' and password == 'password':
            return dcc.Location(pathname='/dashboard', id='dashboard-url')
        else:
            return html.Div('Invalid login credentials. Please try again.')

@app.callback(Output('url', 'pathname'), Input('dashboard-url', 'pathname'))
def redirect_to_dashboard(pathname):
    return pathname

if __name__ == '__main__':
    app.run_server(debug=True)