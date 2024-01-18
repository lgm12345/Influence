import pandas as pd
from pyspark.sql import SparkSession
import pyspark.sql.functions as f
import dash
from dash import Input,Output,html,dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pyspark import SparkConf
import os
import findspark
import locale
from pyspark.sql.types import StringType
from app import app

#app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE])

locale.setlocale(locale.LC_ALL,"pt_BR.UTF-8")

#----------------------------------------instanciação da sessão spark-----------------------------------------------------------#
os.environ["SPARK_HOME"] = '/home/lucas/spark'
findspark.init()
spark = SparkSession.builder \
.config("spark.driver.bindAdress","localhost") \
.config("spark.ui.port", "4052")\
.config("spark.port.maxRetries","100") \
.appName("Analise temporal")\
.getOrCreate()

def formatar_valor(valor):
    return '{:,.2f}'.format(valor).replace(',', '#').replace('.', ',').replace('#', '.')


#registrando a udf
formatar_valor_udf = f.udf(formatar_valor, returnType=StringType())

#-------------------------------------------------Leitura dos dados-------------------------------------------------------------------------------#


df_cliente = spark.read.csv("dados/tabela_cliente_segmento.csv", header=True, inferSchema=True)
df_venda = spark.read.csv("dados/dados_marco.csv", header=True, inferSchema=True)
df = df_venda.join(df_cliente, on="id_cliente", how="inner")
df_grouped = df.groupBy('Classe', 'data').agg(f.sum('valor').alias('valor_total'))
df_grouped = df_grouped.withColumn("valor_total_formatado", formatar_valor_udf("valor_total"))
cores = ["#006400", "#DC143C", "#4169E1", "#FF4500", "#800020", "#FFDB58", "#2E8B57", "#32CD32", "#F5F5F5"]
fig = make_subplots(rows=len(df_grouped.select("Classe").distinct().collect()), cols=1, shared_xaxes=True)
for i, classe_row in enumerate(df_grouped.select("Classe").distinct().collect()):
    classe = classe_row["Classe"]
    text = str(classe)
    data_classe = df_grouped.filter(f.col('Classe') == classe).orderBy('data')
    trace = go.Scatter(
        x=data_classe.select("data").rdd.flatMap(lambda x: x).collect(),
        y=data_classe.select("valor_total").rdd.flatMap(lambda x: x).collect(),
        mode="lines",
        marker_color=cores[i],
        name=text,
        line=dict(width=4),
        hovertemplate="Data: %{x}<br>Valor Total: %{y}",
    )

    fig.add_trace(trace, row=i + 1, col=1)
fig.update_layout(
    height=180*len(df_grouped.select("Classe").distinct().collect()),  # Ajustar a altura da figura conforme o número de classes
    showlegend=True,  # Se quiser mostrar a legenda, altere para True
    paper_bgcolor='rgb(17,17,17)',  # Cor escura de fundo
    plot_bgcolor='rgb(17,17,17)' ,   # Cor escura de fundo para o gráfico em si
    margin=dict(l=80, r=20, t=35, b=20),
    font=dict(color="#FF8C00")

)
for i, classe in enumerate(df_grouped.select("Classe").distinct().collect()):
    fig.add_annotation(
        xref="paper", yref="paper",
        x=-0.12, y=1 - (i / len(df_grouped.select("Classe").distinct().collect())),
        text=text,
        showarrow=False,
        xanchor="center", yanchor="middle"
    )
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)








#------------------------------------------------------Montagem do gráficos-----------------------------------------------------------------------#









#-----------------------------------------------------Configuração do layout----------------------------------------------------------------------#


layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            html.H2("Analise Temporal",style={"font-size":"25px","color":"#FF8C00"})
        ],style={"border": "17px solid transparent","background-color":"#000000"})
    ]),
    dbc.Row(dbc.Col(style={"border": "14px solid transparent","background-color":"#000000"})),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph",figure=fig)
        ],width=12,style={"border": "17px solid transparent","background-color":"#000000"})
    ])
],fluid=True)


#if __name__ == "__main__":
    #app.run_server(debug=True)

