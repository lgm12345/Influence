import pandas as pd
import dash
from dash import Input,Output,html,dcc
import dash_bootstrap_components as dbc
from app import app
#-----------------------------------------------Instanciação do app------------------------------------------------------------------------------#

#app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE])

#-----------------------------------------------Funções auxiliares-------------------------------------------------------------------------------#

def adiciona_rfv(x):
    return str(x["R quintil"]) + " " + str(x["F quintil"]) +  " " + str(x["V quintil"])

#----------------------------------------------Leitura dos dados----------------------------------------------------------------------------------#

df = pd.read_csv("dados/tabela_cliente_segmento.csv")
df["R F V"] = df.apply(adiciona_rfv,axis=1)
df["ticket_medio"] = df["ticket_medio"].apply(lambda x:round(x,2))
df = df.drop(columns=["nr_cpf_cnpj","R quintil","F quintil","V quintil","Frequencia","Outlier"],axis=1)
df = df.rename(columns={"id_cliente":"Id Cliente","faixa_etaria":"Faixa Etária","Classe":"Segmento","cidade":"Cidade","valor_monetario":"Faturamento","ticket_medio":"Ticket Médio","Recência":"R",})
cidades = list(df["Cidade"].unique())
segmentos = list(df["Segmento"].unique())
faixas_etarias = list(df["Faixa Etária"].unique())
#-----------------------------------------------Montagem da tabela--------------------------------------------------------------------------------#







layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Dropdown(
                                id="select-cidade",
                                multi=False,
                                clearable=False,
                                value = cidades[-1],
                                options=[{"label":x,"value":x} for x in cidades],
                                style={"background-color":"lightgray","color":"black"}
                            )
                        ],style={"padding-top":"0px","padding-left":"0px","background-color":"black"})
                    ],style={"height":"6vh"})
                ],width=4),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Dropdown(
                                id="select-faixa-etaria",
                                multi=False,
                                clearable=False,
                                value=faixas_etarias[0],
                                options=[{"label":x,"value":x} for x in faixas_etarias],
                                style={"background-color":"lightgray","color":"black"}
                            )                           
                        ],style={"padding-top":"0px","padding-left":"0px","background-color":"black"})
                    ],style={"height":"6vh"})
                ],width=4),
                dbc.Col([
                    dbc.CardHeader([
                        html.P("Segmento")
                    ]),
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Dropdown(
                                id="select-segmento",
                                multi=False,
                                clearable=False,
                                value=segmentos[0],
                                options=[{"label":x,"value":x} for x in segmentos],
                                style={"background-color":"lightgray","color":"black"}
                            )                            
                        ],style={"padding-top":"0px","padding-left":"0px","background-color":"black"})
                    ],style={"height":"6vh"})
                ],width=4)
            ],className="g-0",style={"background-color":"black"}),
            dbc.Row(dbc.Col(style={"border": "17px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([
                    html.Div(id="tabela")
                ])
            ],style={"background-color":"black"})
        ])
    ],style={"background-color":"black"})
],fluid=True)

@app.callback(
    Output(component_id="tabela",component_property="children"),
    [Input(component_id="select-cidade",component_property="value"),
     Input(component_id="select-faixa-etaria",component_property="value"),
     Input(component_id="select-segmento",component_property="value")]
)

def monta_tabela(cidade,faixa_etaria,segmento):
    df_filtrado = df[(df["Cidade"] == cidade) & (df["Faixa Etária"] == faixa_etaria) & (df["Segmento"] == segmento)]
    children = [
        dbc.Table.from_dataframe(df_filtrado,bordered=True,striped=True,hover=True,style={"font-size":"15px"})
    ]
    return children 

#if __name__ == "__main__":
    #app.run_server(debug=True)