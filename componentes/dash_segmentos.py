import pandas as pd
import dash
from dash import Input,Output,State,html,dcc
import dash_bootstrap_components as dbc
import locale
from app import app
#--------------------------------S-------------------Leitura dos dados----------------------------------------------------------------------------#

df = pd.read_csv("dados/tabela_cliente_segmento.csv")

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE])



#---------------------------------------------------Calculo dos valores por grupo---------------------------------------------------------------#
dic_faturamento_classe = {}
dic_porcentagem_faturamento_classe ={}
dic_qtde_classe = {}
dic_porcentagem_quantidade_classe = {}
df_outlier = df[df["Outlier"] == "Sim"]
df_nao_outlier = df[df["Outlier"] == "Não"]
faturamento_outlier = round(df_outlier["valor_monetario"].sum(),2)
faturamento_outlier = locale.format_string('%.2f',faturamento_outlier,grouping=True)
dic_faturamento_classe["Outlier"] = faturamento_outlier 
dic_porcentagem_faturamento_classe["Outlier"] = round((df_outlier["valor_monetario"].sum()/df["valor_monetario"].sum()),2)
dic_porcentagem_quantidade_classe["Outlier"] = round((df_outlier.shape[0]/df.shape[0]),2)
qtde_outlier = df_outlier.shape[0]
qtde_outlier = locale.format_string('%.0f',qtde_outlier,grouping=True)
dic_qtde_classe["Outlier"] = qtde_outlier


for classe in list(df["Classe"].unique()):
    if (classe != " "):
        faturamento_classe = round(df_nao_outlier[df_nao_outlier["Classe"] == classe]["valor_monetario"].sum(),2)
        faturamento_classe = locale.format_string('%.2f',faturamento_classe,grouping=True)
        dic_faturamento_classe[classe] = faturamento_classe
        dic_porcentagem_faturamento_classe[classe] = round((df_nao_outlier[df_nao_outlier["Classe"] == classe]["valor_monetario"].sum()/df["valor_monetario"].sum()),2)
        qtde_classe = df_nao_outlier[df_nao_outlier["Classe"] == classe].shape[0]
        qtde_classe = locale.format_string('%.0f',qtde_classe,grouping=True)
        dic_qtde_classe[classe] = qtde_classe
        dic_porcentagem_quantidade_classe[classe] = round((df_nao_outlier[df_nao_outlier["Classe"] == classe].shape[0]/df.shape[0]),2)

#---------------------------------------Funções de montagem dos cards de faturamento e quantidade de clientes-----------------------------------#
def monta_card_qtde_clientes(df_nao_outlier,df_outlier,classe,cor_botao):
    total_clientes = df_nao_outlier.shape[0] + df_outlier.shape[0]
    if (classe == "Outlier"):
        qtde_clientes = df_outlier.shape[0]
        qtde_clientes_formatado = locale.format_string('%.0f',qtde_clientes,grouping=True)
        conteudo_card = html.Div([
                            html.Button(style={"background-color":cor_botao,"width": f'{(qtde_clientes * 600)/total_clientes}px', "height": "40px","border":"none"},id=f'botao-quantidade-{classe}'),
                            html.P(f'{qtde_clientes_formatado}', style={"margin-left": "5px","margin-top":"10px","font-size":"10px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
    else: 
        df_filt = df_nao_outlier[df_nao_outlier["Classe"] == classe]
        qtde_clientes = df_filt.shape[0]
        qtde_clientes_formatado = locale.format_string('%.0f',qtde_clientes,grouping=True)
        conteudo_card = html.Div([
                            html.Button(style={"background-color":cor_botao,"width": f'{(qtde_clientes * 600)/total_clientes}px', "height": "40px","border":"none"},id=f'botao-quantidade-{classe}'),
                            html.P(f'{qtde_clientes_formatado}', style={"margin-left": "5px","margin-top":"10px","font-size":"10px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
    
    return conteudo_card

def monta_card_faturamento_clientes(df_nao_outlier,df_outlier,classe,cor_botao):
    faturamento_total  = df_nao_outlier["valor_monetario"].sum() + df_outlier["valor_monetario"].sum()
    if (classe == "Outlier"):
        faturamento_classe = df_outlier["valor_monetario"].sum()
        faturamento_formatado = locale.format_string('%.2f',faturamento_classe,grouping=True)
        conteudo_card = html.Div([
                        html.Button(style={"background-color":cor_botao,"width": f'{(faturamento_classe * 480)/faturamento_total}px', "height": "40px","border":"none"},id=f'botao-faturamento-{classe}'),
                        html.P(f'R$ {faturamento_formatado}', style={"margin-left": "5px","margin-top":"10px","font-size":"10px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
    else:
        df_filt = df_nao_outlier[df_nao_outlier["Classe"] == classe]
        faturamento_classe = round(df_filt["valor_monetario"].sum(),2)
        faturamento_formatado = locale.format_string('%.2f',faturamento_classe,grouping=True)
        conteudo_card = html.Div([
                        html.Button(style={"background-color":cor_botao,"width": f'{(faturamento_classe * 480)/faturamento_total}px', "height": "40px","border":"none"},id=f'botao-faturamento-{classe}'),
                        html.P(f'R$ {faturamento_formatado}', style={"margin-left": "5px","margin-top":"10px","font-size":"10px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
    
    return conteudo_card

#-----------------------------------------------Configuração do Layout---------------------------------------------------------------------------#


layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dbc.Row([
                 dbc.Col([
                    html.H3("RECÊNCIA / FREQUÊNCIA/ VALOR - SEGMENTAÇÃO",style={"font-size":"20px","color":"#FF8C00"})
                 ],width=5),
                 dbc.Col([
                     
                 ],width=7)
            ],style={"background-color":"#000000"}),
            dbc.Row(dbc.Col(style={"border": "17px solid transparent","background-color":"#000000"})), 
            dbc.Row([
                dbc.Col([
                    dbc.CardHeader("Segmento",style={"font-size":"13px","color":"#FF8C00"}),
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Campeão",style={"font-size":"16px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.CardHeader("Descrição",style={"font-size":"13px","color":"#FF8C00"}),
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Melhores clientes",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.CardHeader("Faturamento",style={"font-size":"13px","color":"#FF8C00"}),
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Campeão","#006400")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"}),
                    dbc.Modal([
                        dbc.ModalBody([
                            html.H6("Descrição segmento:     Melhores clientes"),
                            html.H6("Segmento:Campeão"),
                            html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Campeão"]}'),
                            html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Campeão"]}'),
                            html.H6(f'Faturamento:{dic_faturamento_classe["Campeão"]} R$'),
                            html.H6(f'Quantidade Clientes:{dic_qtde_classe["Campeão"]}')
                        ])
                    ],id="modal-faturamento-campeao")
                ],width=3),
                dbc.Col([
                    dbc.CardHeader("Clientes",style={"font-size":"13px","color":"#FF8C00"}),
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Campeão","#006400"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:     Melhores clientes"),
                                html.H6("Segmento:               Campeão"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Campeão"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Campeão"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Campeão"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Campeão"]}')
                        ])
                    ],id="modal-quantidade-campeao")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.CardHeader("Ação recomendada",style={"font-size":"13px","color":"#FF8C00"}),
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Ofereça cross-selling ou up-selling",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=4)
            ],className="g-0",style={"background-color":"#000000"}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Outlier",style={"font-size":"16px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Gasto 2-desvio padrão acima da média",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Outlier","#4169E1"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento: Gastos dois desvio padrão acima da média"),
                                html.H6("Segmento:Outlier"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Outlier"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Outlier"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Outlier"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Outlier"]}')
                        ])
                    ],id="modal-faturamento-outlier")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Outlier","#4169E1"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento: Gastos dois desvio padrão acima da média"),
                                html.H6("Segmento:Outlier"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Outlier"]}'),
                                html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Outlier"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Outlier"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Outlier"]}')
                        ])
                    ],id="modal-quantidade-outlier")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Ofereça promoções personalizadas,contato direto",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=4)
            ],className="g-0"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Em risco",style={"font-size":"16px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Ex-campeão que está abandonado",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Em Risco","#DC143C"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento: Ex-campeão que está abandonado"),
                                html.H6("Segmento:Em Risco"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Em Risco"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Em Risco"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Em Risco"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Em Risco"]}')
                        ])
                    ],id="modal-faturamento-em-risco")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Em Risco","#DC143C"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento: Ex-campeão que está abandonado"),
                                html.H6("Segmento:Em Risco"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Em Risco"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Em Risco"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Em Risco"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Em Risco"]}')
                        ])
                    ],id="modal-quantidade-em-risco")
                            
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Realize campanhas para produtos já consumidos para reconquistá-lo",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=4)
            ],className="g-0",style={"background-color":"#000000"}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Cliente novo",style={"font-size":"15px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Comprara recentemente,mas sem muito histórico",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Cliente Novo","#FFDB58"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento: Comprara recentemente,mas sem muito histórico"),
                                html.H6("Segmento:Cliente Novo"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Cliente Novo"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Cliente Novo"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Cliente Novo"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Cliente Novo"]}')
                        ])
                    ],id="modal-faturamento-cliente-novo")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Cliente Novo","#FFDB58"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento: Comprara recentemente,mas sem muito histórico"),
                                html.H6("Segmento:Cliente Novo"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Cliente Novo"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Cliente Novo"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Cliente Novo"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Cliente Novo"]}')
                        ])
                    ],id="modal-quantidade-cliente-novo")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Dê boas vindas, comece a construir um relacionamento",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=4)
            ],className="g-0"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Incerto",style={"font-size":"16px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Não temos como saber",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Incerto","#FF4500"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Não temos como saber"),
                                html.H6("Segmento:Incerto"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Incerto"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Incerto"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Incerto"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Incerto"]}')
                        ])
                    ],id="modal-faturamento-incerto")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Incerto","#FF4500"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Não temos como saber"),
                                html.H6("Segmento:Incerto"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Incerto"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Incerto"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Incerto"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Incerto"]}')
                        ])
                    ],id="modal-quantidade-incerto")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Estreite a relação com campanhas de promoção",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=4)
            ],className="g-0",style={"background-color":"#000000"}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Valioso",style={"font-size":"16px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Gasta muito bem e é fiel",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Valioso","#2E8B57"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Gasta muito bem e é fiel"),
                                html.H6("Segmento:Valioso"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Valioso"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Valioso"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Valioso"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Valioso"]}')
                        ])
                    ],id="modal-faturamento-valioso")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Valioso","#2E8B57"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Gasta muito bem e é fiel"),
                                html.H6("Segmento:Valioso"),
                                html.H6(f'% do total do faturamento:{100*dic_porcentagem_faturamento_classe["Valioso"]}'),
                                html.H6(f'% da quantidade de clientes:{100*dic_porcentagem_quantidade_classe["Valioso"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Valioso"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Valioso"]}')
                        ])
                    ],id="modal-quantidade-valioso")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Ofereça produtos relevantes e descontos especiais",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=4)
            ],className="g-0"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Não perder",style={"font-size":"15px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Cliente com potencial para ser Campeão",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Não Perder","#800020"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Cliente com potencial para ser Campeão"),
                                html.H6("Segmento:Não Perder"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Não Perder"]}'),
                                html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Não Perder"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Não Perder"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Não Perder"]} R$')
                        ])
                    ],id="modal-faturamento-nao-perder")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Não Perder","#800020"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Cliente com potencial para ser Campeão"),
                                html.H6("Segmento:Não Perder"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Não Perder"]}'),
                                html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Não Perder"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Não Perder"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Não Perder"]} R$')
                        ])
                    ],id="modal-quantidade-nao-perder")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Identifique as marcas preferidas,ofereça amostras grátis",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=4)
            ],className="g-0",style={"background-color":"#000000"}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Promissor",style={"font-size":"15px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Cliente com potencial para ser Campeão",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Promissor"," #32CD32"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Cliente com potencial para ser Campeão"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Promissor"]}'),
                                html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Promissor"]}'),
                                html.H6("Segmento:Promissor"),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Promissor"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Promissor"]} R$')
                        ])
                    ],id="modal-faturamento-promissor")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Promissor"," #32CD32"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Cliente com potencial para ser Campeão"),
                                html.H6("Segmento:Promissor"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Promissor"]}'),
                                html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Promissor"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Promissor"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Promissor"]} R$')
                        ])
                    ],id="modal-quantidade-promissor")
                        ])
                    ],style={"height":"10vh"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Realize campanhas de cross-selling com desconto",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh"})
                ],width=4)                
            ],className="g-0"),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3("Adormecido",style={"font-size":"15px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Menores scores de recência,frequência e valor",style={"font-size":"10px"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=1),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_faturamento_clientes(df_nao_outlier,df_outlier,"Adormecido","#F5F5F5"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Menores scores de recência,frequência e valor"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Adormecido"]}'),
                                html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Adormecido"]}'),
                                html.H6("Segmento:Adormecido"),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Adormecido"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Adormecido"]} R$')
                        ])
                    ],id="modal-faturamento-adormecido")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            monta_card_qtde_clientes(df_nao_outlier,df_outlier,"Adormecido","#F5F5F5"),
                            dbc.Modal([
                                dbc.ModalBody([
                                html.H6("Descrição segmento:Menores scores de recência,frequência e valor"),
                                html.H6("Segmento:Adormecido"),
                                html.H6(f'% do total do faturamento:{dic_porcentagem_faturamento_classe["Adormecido"]}'),
                                html.H6(f'% da quantidade de clientes:{dic_porcentagem_quantidade_classe["Adormecido"]}'),
                                html.H6(f'Faturamento:{dic_faturamento_classe["Adormecido"]} R$'),
                                html.H6(f'Quantidade Clientes:{dic_qtde_classe["Adormecido"]} R$')
                        ])
                    ],id="modal-quantidade-adormecido")
                        ])
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=3),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Reviver com campanha,em outro caso ignorar",style={"font-size":"15px","color":"#FF8C00"},className="card-text")
                        ],className="h-100 d-flex align-items-center justify-content-start")
                    ],style={"height":"10vh","background-color":"#000000"})
                ],width=4)
            ],className="g-0",style={"background-color":"#000000"})
        ])
    ],style={"background-color":"#000000"})
],fluid=True)


@app.callback(
    Output(component_id="modal-faturamento-campeao",component_property="is_open"),
    Input(component_id="botao-faturamento-Campeão",component_property="n_clicks"),
    State(component_id="modal-faturamento-campeao",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-campeao",component_property="is_open"),
    Input(component_id="botao-quantidade-Campeão",component_property="n_clicks"),
    State(component_id="modal-quantidade-campeao",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-faturamento-outlier",component_property="is_open"),
    Input(component_id="botao-faturamento-Outlier",component_property="n_clicks"),
    State(component_id="modal-faturamento-outlier",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-outlier",component_property="is_open"),
    Input(component_id="botao-quantidade-Outlier",component_property="n_clicks"),
    State(component_id="modal-quantidade-outlier",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open
    
@app.callback(
    Output(component_id="modal-faturamento-em-risco",component_property="is_open"),
    Input(component_id="botao-faturamento-Em Risco",component_property="n_clicks"),
    State(component_id="modal-faturamento-em-risco",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-em-risco",component_property="is_open"),
    Input(component_id="botao-quantidade-Em Risco",component_property="n_clicks"),
    State(component_id="modal-quantidade-em-risco",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open


@app.callback(
    Output(component_id="modal-faturamento-cliente-novo",component_property="is_open"),
    Input(component_id="botao-faturamento-Cliente Novo",component_property="n_clicks"),
    State(component_id="modal-faturamento-cliente-novo",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-cliente-novo",component_property="is_open"),
    Input(component_id="botao-quantidade-Cliente Novo",component_property="n_clicks"),
    State(component_id="modal-quantidade-cliente-novo",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-faturamento-incerto",component_property="is_open"),
    Input(component_id="botao-faturamento-Incerto",component_property="n_clicks"),
    State(component_id="modal-faturamento-incerto",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-incerto",component_property="is_open"),
    Input(component_id="botao-quantidade-Incerto",component_property="n_clicks"),
    State(component_id="modal-quantidade-incerto",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open
    
@app.callback(
    Output(component_id="modal-faturamento-valioso",component_property="is_open"),
    Input(component_id="botao-faturamento-Valioso",component_property="n_clicks"),
    State(component_id="modal-faturamento-valioso",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open
    
@app.callback(
    Output(component_id="modal-quantidade-valioso",component_property="is_open"),
    Input(component_id="botao-quantidade-Valioso",component_property="n_clicks"),
    State(component_id="modal-quantidade-valioso",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open



@app.callback(
    Output(component_id="modal-faturamento-nao-perder",component_property="is_open"),
    Input(component_id="botao-faturamento-Não Perder",component_property="n_clicks"),
    State(component_id="modal-faturamento-nao-perder",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-nao-perder",component_property="is_open"),
    Input(component_id="botao-quantidade-Não Perder",component_property="n_clicks"),
    State(component_id="modal-quantidade-nao-perder",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-faturamento-promissor",component_property="is_open"),
    Input(component_id="botao-faturamento-Promissor",component_property="n_clicks"),
    State(component_id="modal-faturamento-promissor",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-promissor",component_property="is_open"),
    Input(component_id="botao-quantidade-Promissor",component_property="n_clicks"),
    State(component_id="modal-quantidade-promissor",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-faturamento-adormecido",component_property="is_open"),
    Input(component_id="botao-faturamento-Adormecido",component_property="n_clicks"),
    State(component_id="modal-faturamento-nao-perder",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

@app.callback(
    Output(component_id="modal-quantidade-adormecido",component_property="is_open"),
    Input(component_id="botao-quantidade-Adormecido",component_property="n_clicks"),
    State(component_id="modal-quantidade-nao-perder",component_property="is_open")
)

def toogle_modal_campeao(n1,is_open):
    if n1:
        return not is_open

#if __name__ == "__main__":
    #app.run_server(debug=True)
