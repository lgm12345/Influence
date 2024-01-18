import dash
import dash_bootstrap_components as dbc
from dash import html,dcc,Input,Output
import os
from app import *
from componentes import barra_navegacao,dash_analise_360,dash_cluster,dash_pontuacoes,dash_segmentos,dash_analise_temporal



#----------------------------------------------Função que define o caminho ate o dashbord selecionado---------------------------------------------#


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            barra_navegacao.layout
        ],className="w-10")
    ],style={"background-color":"#000000"},className="g-0"),
    dbc.Row([
        dbc.Col([
            html.Div(id="page-content")
        ],className="w-10")
    ],style={"background-color":"#000000"},className="g-0")
],fluid=True,style={"background-color":"#000000"})

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if (pathname == "/"):
        return dash_segmentos.layout
    elif (pathname == "/dash_segmentos"):
        return dash_segmentos.layout
    elif (pathname == "/dash_pontuacoes") :
        return dash_pontuacoes.layout
    elif (pathname == "/dash_analise_360"):
        return dash_analise_360.layout
    elif (pathname == "/dash_cluster"):
        return dash_cluster.layout
    elif (pathname == "/dash_analise_temporal"):
        return dash_analise_temporal.layout
        



if __name__ == "__main__":
    app.run_server(debug=True)

