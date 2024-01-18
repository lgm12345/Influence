import pandas as pd
import dash
from dash import Input,Output,html,dcc
import dash_bootstrap_components as dbc




layout = dbc.Container(children=[
    html.Nav(
        children=[
            dcc.Link("Segmentos RFV", href="/dash_segmentos", className='menu-link',style={"margin-right":"5px"}),
            dcc.Link("Pontuações RFV", href="/dash_pontuacoes", className='menu-link',style={"margin-right":"5px"}),
            dcc.Link("Analise 360", href="/dash_analise_360", className='menu-link',style={"margin-right":"5px"}),
            dcc.Link("Analise Temporal", href="/dash_analise_temporal", className='menu-link',style={"margin-right":"5px"}),
            dcc.Link("Cluster de Clientes", href="/dash_cluster", className='menu-link',style={"margin-right":"5px"})
        ],
        className='menu-container',
        style={"background-color":"#000000"}
    )
],fluid=True,style={"background-color":"#000000"})