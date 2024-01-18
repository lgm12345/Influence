import pandas as pd
import dash
from dash import Input,Output,State,html,dcc
import dash_bootstrap_components as dbc
from app import app

#app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE])



#---------------------------------------------------------Instanciação do dashbord-----------------------------------------------------------------#

layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#808080","width": "25px", "height": "25px","border":"none"},id="botao-adormecido"),
                        html.P("Adormecido", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ]),
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#006400","width": "25px", "height": "25px","border":"none"},id="botao-campeao"),
                        html.P("Campeão", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ]),
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#ADFF2F","width": "25px", "height": "25px","border":"none"},id="botao-cliente-novo"),
                        html.P("Cliente novo", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ]),
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#FF0000","width": "25px", "height": "25px","border":"none"},id="botao-em-risco"),
                        html.P("Em risco", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ]),
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#FF8C00","width": "25px", "height": "25px","border":"none"},id="botao-incerto"),
                        html.P("Incerto", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ]),
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#A52A2A","width": "25px", "height": "25px","border":"none"},id="botao-nao-perder"),
                        html.P("Não perder", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ]),
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#32CD32","width": "25px", "height": "25px","border":"none"},id="botao-valioso"),
                        html.P("Valioso", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ]),
                dbc.Col([
                    html.Div([
                        html.Button(style={"background-color":"#8FBC8F","width": "25px", "height": "25px","border":"none"},id="botao-promissor"),
                        html.P("Promissor", style={"margin-left": "5px","margin-top":"10px","font-size":"15px"})
                    ],style={"display": "flex", "flex-direction": "row", "align-items": "center"})
                ])
            ],className="g-0"),
            dbc.Row(dbc.Col(style={"border": "10px solid transparent"})), 
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.H3("Pontuação R",style={"font-size":"20px"})
                    ],style={"text-align":"center"})
                ],width=2),
                dbc.Col([
                    html.Div([
                        html.H3("Pontuação F",style={"font-size":"20px"})
                    ],style={"text-align":"center"})                
                ],width=3),
                dbc.Col([
                    html.Div([
                        html.H3("Pontuação V",style={"font-size":"20px","margin-top":"-15px"}),
                        dbc.Row([
                            dbc.Col([
                                html.H4("5",style={"font-size":"20px"})
                            ]),
                            dbc.Col([
                                html.H4("4",style={"font-size":"20px"})
                            ]),
                            dbc.Col([
                                html.H4("3",style={"font-size":"20px"})
                            ]),
                            dbc.Col([
                                html.H4("2",style={"font-size":"20px"})
                            ]),
                            dbc.Col([
                                html.H4("1",style={"font-size":"20px"})
                            ])
                        ])
                    ],style={"text-align":"center"})
                ],width=7)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.H3("5",style={"font-size":"15px"})
                                ]),
                                dbc.Col([
                                    html.H3("5",style={"font-size":"15px"}),
                                    html.H3("4",style={"font-size":"15px"}),
                                    html.H3("3",style={"font-size":"15px"}),
                                    html.H3("2",style={"font-size":"15px"}),
                                    html.H3("1",style={"font-size":"15px"})
                                ])
                            ])
                        ])
                    ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
                ],width=5),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col([
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-1"),
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-2"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-1"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-2"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-3")

                                ]),
                                dbc.Col([
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-3"),
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-4"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-4"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-5"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-6")

                                ]),
                                dbc.Col([
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-1"),
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-2"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-1"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-2"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-3")
                                ]),
                                dbc.Col([
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-3"),
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-4"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-4"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-5"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-6")
                                ]),
                                dbc.Col([
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-5"),
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-6"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-7"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-8"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-9")
                                ])
                            ])
                        ])
                    ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
                ],width=7)
        ],className="g-0"),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.H3("4",style={"font-size":"15px"})
                            ]),
                            dbc.Col([
                                html.H3("5",style={"font-size":"15px"}),
                                html.H3("4",style={"font-size":"15px"}),
                                html.H3("3",style={"font-size":"15px"}),
                                html.H3("2",style={"font-size":"15px"}),
                                html.H3("1",style={"font-size":"15px"})
                                ])
                            ])
                        ])
                    ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=5),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-5"),
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-6"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-7"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-8"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-9")
                            ]),
                            dbc.Col([
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-7"),
                                    html.H3("Campeão",style={"font-size":"15px","color":"#006400"},id="card-campeao-8"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-10"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-11"),
                                    html.H3("Valioso",style={"font-size":"15px","color":"#32CD32"},id="card-valioso-12")
                            ]),
                            dbc.Col([
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-7"),
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-8"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-10"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-11"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-12")
                            ]),
                            dbc.Col([
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-9"),
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-10"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-13"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-14"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-15")
                            ]),
                            dbc.Col([
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-11"),
                                    html.H3("Promissor",style={"font-size":"15px","color":"#8FBC8F"},id="card-promissor-12"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-16"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-17"),
                                    html.H3("Cliente Novo",style={"font-size":"15px","color":"#ADFF2F"},id="card-cliente-novo-18")
                            ])
                        ])
                    ])
                ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=7)
        ],className="g-0"),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.H3("3",style={"font-size":"15px"})
                            ]),
                            dbc.Col([
                                html.H3("5",style={"font-size":"15px"}),
                                html.H3("4",style={"font-size":"15px"}),
                                html.H3("3",style={"font-size":"15px"}),
                                html.H3("2",style={"font-size":"15px"}),
                                html.H3("1",style={"font-size":"15px"})
                                ])
                            ])
                        ])
                    ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=5),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-1"),
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-2"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-1"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-2"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-3")
                            ]),
                            dbc.Col([
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-3"),
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-4"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-4"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-5"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-6")
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-1"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-2"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-1"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-2"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-3")                               
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-3"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-4"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-4"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-5"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-6")   
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-5"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-6"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-7"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-8"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-9")  
                            ])
                        ])
                    ])
                ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=7)
        ],className="g-0"),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.H3("2",style={"font-size":"15px"})
                            ]),
                            dbc.Col([
                                html.H3("5",style={"font-size":"15px"}),
                                html.H3("4",style={"font-size":"15px"}),
                                html.H3("3",style={"font-size":"15px"}),
                                html.H3("2",style={"font-size":"15px"}),
                                html.H3("1",style={"font-size":"15px"})
                                ])
                            ])
                        ])
                    ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=5),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-5"),
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-6"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-7"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-8"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-9")
                            ]),
                            dbc.Col([
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-7"),
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-8"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-10"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-11"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-12")
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-7"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-8"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-10"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-11"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-12")   
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-9"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-10"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-13"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-14"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-15")   
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-11"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-12"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-16"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-17"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-18") 
                            ])
                        ])
                    ])
                ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=7)
        ],className="g-0"),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.H3("1",style={"font-size":"15px"})
                            ]),
                            dbc.Col([
                                html.H3("5",style={"font-size":"15px"}),
                                html.H3("4",style={"font-size":"15px"}),
                                html.H3("3",style={"font-size":"15px"}),
                                html.H3("2",style={"font-size":"15px"}),
                                html.H3("1",style={"font-size":"15px"})
                                ])
                            ])
                        ])
                    ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=5),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dbc.Row([
                            dbc.Col([
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-9"),
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-10"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-13"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-14"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-15")
                            ]),
                            dbc.Col([
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-11"),
                                html.H3("Em Risco",style={"font-size":"15px","color":"#FF0000"},id="card-em-risco-12"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-16"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-17"),
                                html.H3("Não Perder",style={"font-size":"15px","color":"#A52A2A"},id="card-nao-perder-18")
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-13"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-14"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-19"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-20"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-21")   
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-15"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-16"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-22"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-23"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-24")   
                            ]),
                            dbc.Col([
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-17"),
                                html.H3("Adormecido",style={"font-size":"15px","color":"#808080"},id="card-adormecido-18"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-25"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-26"),
                                html.H3("Incerto",style={"font-size":"15px","color":"#FF8C00"},id="card-incerto-27") 
                            ])
                        ])
                    ])
                ],style={"background-color":"#000000","border-color":"white","height":"23vh"})
            ],width=7)
        ],className="g-0")
    ])
],style={"background-color":"#000000"})
],fluid=True)


@app.callback(
    [Output(component_id="card-campeao-1",component_property="style"),
     Output(component_id="card-campeao-2",component_property="style"),
     Output(component_id="card-campeao-3",component_property="style"),
     Output(component_id="card-campeao-4",component_property="style"),
     Output(component_id="card-campeao-5",component_property="style"),
     Output(component_id="card-campeao-6",component_property="style"),
     Output(component_id="card-campeao-7",component_property="style"),
     Output(component_id="card-campeao-8",component_property="style")],
     Input(component_id="botao-campeao",component_property="n_clicks")

)

def ofuscar_card_campeao(n_clicks):
    if n_clicks is None:
        return [{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"}]
    elif n_clicks % 2 == 1:
        return [{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#006400","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"}]
    else :
        return [{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"},{"font-size":"15px","color":"#006400","text-align":"center"}]


@app.callback(
    [Output(component_id="card-valioso-1",component_property="style"),
     Output(component_id="card-valioso-2",component_property="style"),
     Output(component_id="card-valioso-3",component_property="style"),
     Output(component_id="card-valioso-4",component_property="style"),
     Output(component_id="card-valioso-5",component_property="style"),
     Output(component_id="card-valioso-6",component_property="style"),
     Output(component_id="card-valioso-7",component_property="style"),
     Output(component_id="card-valioso-8",component_property="style"),
     Output(component_id="card-valioso-9",component_property="style"),
     Output(component_id="card-valioso-10",component_property="style"),
     Output(component_id="card-valioso-11",component_property="style"),
     Output(component_id="card-valioso-12",component_property="style"),
     Input(component_id="botao-valioso",component_property="n_clicks")]
)

def ofuscar_card_valioso(n_clicks):
    if n_clicks is None:
        return [{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"}]
    elif n_clicks % 2 == 1:
        return [{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},{"font-size":"15px","color":"#32CD32","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"}]
    else :
        return [{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"},{"font-size":"15px","color":"#32CD32","text-align":"center"}]

@app.callback(
    [Output(component_id="card-em-risco-1",component_property="style"),
     Output(component_id="card-em-risco-2",component_property="style"),
     Output(component_id="card-em-risco-3",component_property="style"),
     Output(component_id="card-em-risco-4",component_property="style"),
     Output(component_id="card-em-risco-5",component_property="style"),
     Output(component_id="card-em-risco-6",component_property="style"),
     Output(component_id="card-em-risco-7",component_property="style"),
     Output(component_id="card-em-risco-8",component_property="style"),
     Output(component_id="card-em-risco-9",component_property="style"),
     Output(component_id="card-em-risco-10",component_property="style"),
     Output(component_id="card-em-risco-11",component_property="style"),
     Output(component_id="card-em-risco-12",component_property="style"),],
     Input(component_id="botao-em-risco",component_property="n_clicks")

)

def ofuscar_card_em_risco(n_clicks):
    if n_clicks is None:
        return [
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"}
]
    elif n_clicks % 2 == 1:
        return [
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","border": "2px solid red", "box-shadow": "0 0 10px red","text-align":"center"}
]

    else :
        [
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"},
  {"font-size":"15px","color":"#FF0000","text-align":"center"}
]

@app.callback(
    [Output(component_id="card-nao-perder-1",component_property="style"),
     Output(component_id="card-nao-perder-2",component_property="style"),
     Output(component_id="card-nao-perder-3",component_property="style"),
     Output(component_id="card-nao-perder-4",component_property="style"),
     Output(component_id="card-nao-perder-5",component_property="style"),
     Output(component_id="card-nao-perder-6",component_property="style"),
     Output(component_id="card-nao-perder-7",component_property="style"),
     Output(component_id="card-nao-perder-8",component_property="style"),
     Output(component_id="card-nao-perder-9",component_property="style"),
     Output(component_id="card-nao-perder-10",component_property="style"),
     Output(component_id="card-nao-perder-11",component_property="style"),
     Output(component_id="card-nao-perder-12",component_property="style"),
     Output(component_id="card-nao-perder-13",component_property="style"),
     Output(component_id="card-nao-perder-14",component_property="style"),
     Output(component_id="card-nao-perder-15",component_property="style"),
     Output(component_id="card-nao-perder-16",component_property="style"),
     Output(component_id="card-nao-perder-17",component_property="style"),
     Output(component_id="card-nao-perder-18",component_property="style")
     ],
     Input(component_id="botao-nao-perder",component_property="n_clicks")
)

def ofuscar_card_nao_perder(n_clicks):
    if n_clicks is None:
        return [
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"}
]
    elif n_clicks % 2 == 1:
        return [
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"}
]

    else :
        return [
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
  {"font-size":"15px","color":"#A52A2A","text-align":"center"},
   {"font-size":"15px","color":"#A52A2A","text-align":"center"}
]



@app.callback(
    [Output(component_id="card-promissor-1",component_property="style"),
     Output(component_id="card-promissor-2",component_property="style"),
     Output(component_id="card-promissor-3",component_property="style"),
     Output(component_id="card-promissor-4",component_property="style"),
     Output(component_id="card-promissor-5",component_property="style"),
     Output(component_id="card-promissor-6",component_property="style"),
     Output(component_id="card-promissor-7",component_property="style"),
     Output(component_id="card-promissor-8",component_property="style"),
     Output(component_id="card-promissor-9",component_property="style"),
     Output(component_id="card-promissor-10",component_property="style"),
     Output(component_id="card-promissor-11",component_property="style"),
     Output(component_id="card-promissor-12",component_property="style"),
     Input(component_id="botao-promissor",component_property="n_clicks")]
)

def ofuscar_card_promissor(n_clicks):
    if n_clicks is None:
        return [
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"}
]
    elif n_clicks % 2 == 1:
        return[
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"}
]

    else :
        return [
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"},
  {"font-size":"15px","color":"#8FBC8F","text-align":"center"}
]


@app.callback(
    [Output(component_id="card-cliente-novo-1",component_property="style"),
     Output(component_id="card-cliente-novo-2",component_property="style"),
     Output(component_id="card-cliente-novo-3",component_property="style"),
     Output(component_id="card-cliente-novo-4",component_property="style"),
     Output(component_id="card-cliente-novo-5",component_property="style"),
     Output(component_id="card-cliente-novo-6",component_property="style"),
     Output(component_id="card-cliente-novo-7",component_property="style"),
     Output(component_id="card-cliente-novo-8",component_property="style"),
     Output(component_id="card-cliente-novo-9",component_property="style"),
     Output(component_id="card-cliente-novo-10",component_property="style"),
     Output(component_id="card-cliente-novo-11",component_property="style"),
     Output(component_id="card-cliente-novo-12",component_property="style"),
     Output(component_id="card-cliente-novo-13",component_property="style"),
     Output(component_id="card-cliente-novo-14",component_property="style"),
     Output(component_id="card-cliente-novo-15",component_property="style"),
     Output(component_id="card-cliente-novo-16",component_property="style"),
     Output(component_id="card-cliente-novo-17",component_property="style"),
     Output(component_id="card-cliente-novo-18",component_property="style")],
     Input(component_id="botao-cliente-novo",component_property="n_clicks")
)

def ofuscar_card_cliente_novo(n_clicks):
    if n_clicks is None:
        return[
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"}
]

    elif n_clicks % 2 == 1:
        return [
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"}
]

    else :
        return [
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"},
  {"font-size":"15px","color":"#ADFF2F","text-align":"center"}
]


@app.callback(
    [Output(component_id="card-adormecido-1",component_property="style"),
     Output(component_id="card-adormecido-2",component_property="style"),
     Output(component_id="card-adormecido-3",component_property="style"),
     Output(component_id="card-adormecido-4",component_property="style"),
     Output(component_id="card-adormecido-5",component_property="style"),
     Output(component_id="card-adormecido-6",component_property="style"),
     Output(component_id="card-adormecido-7",component_property="style"),
     Output(component_id="card-adormecido-8",component_property="style"),
     Output(component_id="card-adormecido-9",component_property="style"),
     Output(component_id="card-adormecido-10",component_property="style"),
     Output(component_id="card-adormecido-11",component_property="style"),
     Output(component_id="card-adormecido-12",component_property="style"),
     Output(component_id="card-adormecido-13",component_property="style"),
     Output(component_id="card-adormecido-14",component_property="style"),
     Output(component_id="card-adormecido-15",component_property="style"),
     Output(component_id="card-adormecido-16",component_property="style"),
     Output(component_id="card-adormecido-17",component_property="style"),
     Output(component_id="card-adormecido-18",component_property="style")
     ],
     Input(component_id="botao-adormecido",component_property="n_clicks")
)

def ofuscar_card_adormecido(n_clicks):
    if n_clicks is None:
        return [
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"}
]

    elif n_clicks % 2 == 1:
        return [
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#808080","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"}
]

    else :
        return [
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"},
  {"font-size":"15px","color":"#808080","text-align":"center"}
]


@app.callback(
    [Output(component_id="card-incerto-1",component_property="style"),
     Output(component_id="card-incerto-2",component_property="style"),
     Output(component_id="card-incerto-3",component_property="style"),
     Output(component_id="card-incerto-4",component_property="style"),
     Output(component_id="card-incerto-5",component_property="style"),
     Output(component_id="card-incerto-6",component_property="style"),
     Output(component_id="card-incerto-7",component_property="style"),
     Output(component_id="card-incerto-8",component_property="style"),
     Output(component_id="card-incerto-9",component_property="style"),
     Output(component_id="card-incerto-10",component_property="style"),
     Output(component_id="card-incerto-11",component_property="style"),
     Output(component_id="card-incerto-12",component_property="style"),
     Output(component_id="card-incerto-13",component_property="style"),
     Output(component_id="card-incerto-14",component_property="style"),
     Output(component_id="card-incerto-15",component_property="style"),
     Output(component_id="card-incerto-16",component_property="style"),
     Output(component_id="card-incerto-17",component_property="style"),
     Output(component_id="card-incerto-18",component_property="style"),
     Output(component_id="card-incerto-19",component_property="style"),
     Output(component_id="card-incerto-20",component_property="style"),
     Output(component_id="card-incerto-21",component_property="style"),
     Output(component_id="card-incerto-22",component_property="style"),
     Output(component_id="card-incerto-23",component_property="style"),
     Output(component_id="card-incerto-24",component_property="style"),
     Output(component_id="card-incerto-25",component_property="style"),
     Output(component_id="card-incerto-26",component_property="style"),
     Output(component_id="card-incerto-27",component_property="style")
     ],
     Input(component_id="botao-incerto",component_property="n_clicks")
)

def ofuscar_card_adormecido(n_clicks):
    if n_clicks is None:
        return [
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"}
]

    elif n_clicks % 2 == 1:
        return [
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","border": "2px solid red", "box-shadow": "0 0 10px red", "text-align":"center"}
]

    else :
        return [
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"},
  {"font-size":"15px","color":"#FF8C00","text-align":"center"}
]


