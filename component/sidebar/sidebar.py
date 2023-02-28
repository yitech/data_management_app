import dash
import dash.html as html
from dash.dependencies import Input, Output, State


sidebar = html.Div(
            children=[
                html.H2(children="Sidebar"),
                html.Ul(
                    children=[
                        html.Li(html.A("Home", href="/")),
                        html.Li(html.A("Login", href="/login")),
                    ]
                )
            ],
            style={
                'position': 'fixed',
                'top': 0,
                'left': 0,
                'bottom': 0,
                'width': '200px',
                'padding': '20px',
                'backgroundColor': '#f0f0f0'
            }
        )