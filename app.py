import dash
import dash.html as html
import dash.dcc as dcc
import dash_bootstrap_components as dbc
from component.sidebar import sidebar
from page.login import login_layout
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

