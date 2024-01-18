import dash
import pandas as pd
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE],suppress_callback_exceptions=True)

app.scripts.config.serve_locally = True

server = app.server