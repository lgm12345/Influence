import pandas as pd
import dash
from dash import Input,Output,html,dcc
import dash_bootstrap_components as dbc
from dash import dash_table
import plotly.graph_objects as go
import os
from app import app
#app = dash.Dash(__name__,external_stylesheets=[dbc.themes.SLATE],suppress_callback_exceptions=True)

#-----------------------------------------------------Leitura dos dados analise geral-----------------------------------------------------------------------#

df = pd.read_csv("dados/tabela_cliente_segmento.csv")   #usado apenas para montagem do grafico
df_regras_associacao = pd.read_parquet("dados/regras_associacao.parquet") #usado para montar a analise da cesta de compra
df_top_setores = pd.read_csv("dados/top_setores.csv")
df_analise_consumo = pd.read_csv("dados/analise_consumo.csv")
maior_lift = df_regras_associacao["lift"].max()
menor_lift = df_regras_associacao["lift"].min()
maior_confidence = df_regras_associacao["confidence"].max()
menor_confidence = df_regras_associacao["confidence"].min()
top_7_setores = df_top_setores.head(7)["ds_classe2"].to_list()

#-------------------------------------------------Leitura dos dados analise setor Campeao--------------------------------------------------------------------#

df_top_setores_campeao = pd.read_csv("dados/top_setores_campeao.csv")
df_analise_consumo_campeao = pd.read_csv("dados/analise_consumo_campeao.csv")
top_7_setores_campeao = df_top_setores_campeao.head(7)["ds_classe2"].to_list()

#-------------------------------------------------Leitura dos dados analise setor Valioso---------------------------------------------------------------------#

df_top_setores_valioso = pd.read_csv("dados/top_setores_valioso.csv")
df_analise_consumo_valioso = pd.read_csv("dados/analise_consumo_valioso.csv")
top_7_setores_valioso = df_top_setores_valioso.head(7)["ds_classe2"].to_list()

#---------------------------------------------------Leitura dos dados analise setor Incerto--------------------------------------------------------------------#

df_top_setores_incerto = pd.read_csv("dados/top_setores_incerto.csv")
df_analise_consumo_incerto = pd.read_csv("dados/analise_consumo_incerto.csv")
top_7_setores_incerto = df_top_setores_incerto.head(7)["ds_classe2"].to_list()

#-----------------------------------------------------Leitura dos dados analise setor Cliente Novo--------------------------------------------------------------#

df_top_setores_cliente_novo = pd.read_csv("dados/top_setores_cliente_novo.csv")
df_analise_consumo_cliente_novo = pd.read_csv("dados/analise_consumo_cliente_novo.csv")
top_7_setores_cliente_novo = df_top_setores_cliente_novo.head(7)["ds_classe2"].to_list()

#-----------------------------------------------------Leitura dos dados analise setor Promissor--------------------------------------------------------------------#

df_top_setores_promissor = pd.read_csv("dados/top_setores_promissor.csv")
df_analise_consumo_promissor = pd.read_csv("dados/analise_consumo_promissor.csv")
top_7_setores_promissor = df_top_setores_promissor.head(7)["ds_classe2"].to_list()

#-----------------------------------------------------Leitura dos dados analise setor Em Risco-----------------------------------------------------------------#

df_top_setores_em_risco = pd.read_csv("dados/top_setores_em_risco.csv")
df_analise_consumo_em_risco = pd.read_csv("dados/analise_consumo_em_risco.csv")
top_7_setores_em_risco = df_top_setores_em_risco.head(7)["ds_classe2"].to_list()

#-----------------------------------------------------Leitura dos dados analise setor Nao Perder----------------------------------------------------------------#

df_top_setores_nao_perder = pd.read_csv("dados/top_setores_nao_perder.csv")
df_analise_consumo_nao_perder = pd.read_csv("dados/analise_consumo_nao_perder.csv")
top_7_setores_nao_perder = df_top_setores_nao_perder.head(7)["ds_classe2"].to_list()

#-----------------------------------------------------Leitura dos dados analise setor Outlier-------------------------------------------------------------------#

df_top_setores_outlier = pd.read_csv("dados/top_setores_outlier.csv")
df_analise_consumo_outlier = pd.read_csv("dados/analise_consumo_outlier.csv")
top_7_setores_outlier = df_top_setores_outlier.head(7)["ds_classe2"].to_list()

#-----------------------------------------------------Leitura dos dados analise setor Adormecido----------------------------------------------------------------#

df_top_setores_adormecido = pd.read_csv("dados/top_setores_adormecido.csv")
df_analise_consumo_adormecido = pd.read_csv("dados/analise_consumo_adormecido.csv")
top_7_setores_adormecido = df_top_setores_adormecido.head(7)["ds_classe2"].to_list()

#----------------------------------------------------funcao auxiliar que monta o card com o nome do setor-------------------------------------------------------#

def monta_card_nome_segmento(i,segmento):
    children = []
    if segmento is None:
        children.append(top_7_setores[i])
        return children 
    elif segmento == "Campeão":
        children.append(top_7_setores_campeao[i])
        return children
    elif segmento == "Valioso":
        children.append(top_7_setores_valioso[i])
        return children
    elif segmento == "Promissor":
        children.append(top_7_setores_promissor[i])
        return children
    elif segmento == "Cliente Novo":
        children.append(top_7_setores_cliente_novo[i])
        return children
    elif segmento == "Não Perder":
        children.append(top_7_setores_nao_perder[i])
        return children
    elif segmento == "Em Risco":
        children.append(top_7_setores_em_risco[i])
        return children
    elif segmento == "Incerto":
        children.append(top_7_setores_incerto[i])
        return children
    elif segmento == "Outlier":
        children.append(top_7_setores_outlier[i])
        return children
    elif segmento == "Adormecido":
        children.append(top_7_setores_adormecido[i])
        return children

#----------------------------------------------funcao auxiliar que monta o card com os indices dos top produtos-------------------------------------------------#

def monta_card_qnt_top_produtos(top_produtos):
    children = []
    for i in range(top_produtos):
        children.append(html.P(f'{i + 1}',style={"font-size":"10px","margin-top":"0px"}))
    card = dbc.CardBody(children=children)
    return card

#----------------------------------------------fucao auxiliar que monta o card com os nomes dos top produtos--------------------------------------------------#

def monta_card_top_produtos(top_produtos,setor,segmento):
    if segmento is None:
        children = []
        df_setor = df_analise_consumo[df_analise_consumo["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Campeão":
        children = []
        df_setor = df_analise_consumo_campeao[df_analise_consumo_campeao["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Valioso":
        children = []
        df_setor = df_analise_consumo_valioso[df_analise_consumo_valioso["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Promissor":
        children = []
        df_setor = df_analise_consumo_promissor[df_analise_consumo_promissor["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Cliente Novo":
        children = []
        df_setor = df_analise_consumo_cliente_novo[df_analise_consumo_cliente_novo["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Não Perder":
        children = []
        df_setor = df_analise_consumo_nao_perder[df_analise_consumo_nao_perder["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Adormecido":
        children = []
        df_setor = df_analise_consumo_adormecido[df_analise_consumo_adormecido["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Incerto":
        children = []
        df_setor = df_analise_consumo_incerto[df_analise_consumo_incerto["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card
    elif segmento == "Outlier":
        children = []
        df_setor = df_analise_consumo_outlier[df_analise_consumo_outlier["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card 
    elif segmento == "Em Risco":
        children = []
        df_setor = df_analise_consumo_em_risco[df_analise_consumo_em_risco["ds_classe2"] == setor]
        df_setor = df_analise_consumo_outlier[df_analise_consumo_outlier["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        for i in range(top_produtos):
            children.append(html.P(df_setor["nm_produto"][i],style={"font-size":"10px"}))
        card = dbc.CardBody(children=children)
        return card 

#----------------------------------funcao auxiliar que monta o card com o grafico com o faturamento dos produtos----------------------------------------------#


def monta_card_grafico(top_produtos,setor,i,segmento):
    dic_cores = {0:"#00CED1",1:"#4169E1",2:"#2E8B57",3:"#DC143C",4:"#FF4500",5:"#FFDB58",6:"#FFB6C1"}
    if segmento is None:
        df_setor = df_analise_consumo[df_analise_consumo["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Campeao":
        df_setor = df_analise_consumo_campeao[df_analise_consumo_campeao["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Valioso":
        df_setor = df_analise_consumo_valioso[df_analise_consumo_valioso["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Promissor":
        df_setor = df_analise_consumo_promissor[df_analise_consumo_promissor["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Cliente Novo":
        df_setor = df_analise_consumo_cliente_novo[df_analise_consumo_cliente_novo["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Em Risco":
        df_setor = df_analise_consumo_em_risco[df_analise_consumo_em_risco["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Incerto":
        df_setor = df_analise_consumo_incerto[df_analise_consumo_incerto["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Adormecido":
        df_setor = df_analise_consumo_adormecido[df_analise_consumo_adormecido["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Outlier":
        df_setor = df_analise_consumo_outlier[df_analise_consumo_outlier["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    elif segmento == "Nao Perder":
        df_setor = df_analise_consumo_nao_perder[df_analise_consumo_nao_perder["ds_classe2"] == setor]
        df_setor = df_setor.sort_values("vl_total",ascending=False).reset_index(drop=True)
        df_filt = df_setor.iloc[:top_produtos]
        produtos = df_filt["nm_produto"].to_list()
        produtos.reverse()
        valores = df_filt["vl_total"].to_list()
        valores.reverse()
        marker_color = []
        cor = dic_cores[i]
        for j in range(top_produtos):
            marker_color.append(cor)
        fig = go.Figure(go.Bar(
            x = valores,
            orientation='h',
            marker_color=marker_color,
            hovertemplate=f'Produto: {produtos[j]} Valor: {valores[j]}',
            name="Descrição"
        ))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',  
            yaxis_title="",
            plot_bgcolor='rgb(17,17,17)',
            height=60*top_produtos,
            margin=dict(t=20,l=0)), 
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False),
        return fig
    
#----------------------------------------funcao auxiliar que monta o grafico do faturamento por faixa etaria-------------------------------------------#
    
def monta_grafico_faturamento_faixa_etaria(segmento):
    if segmento is None:
        df_agregado = df.groupby("faixa_etaria").agg({"ticket_medio":"mean","valor_monetario":"sum"}).reset_index()
        faixas_etarias = df_agregado["faixa_etaria"].to_list()
        faturamentos = df_agregado["valor_monetario"].to_list()
        fig = go.Figure(go.Bar(x=faixas_etarias,y=faturamentos,orientation="v"))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',
            plot_bgcolor='rgb(17,17,17)',
            yaxis_title=""
        )
        return fig
    else:
        df_agregado = df[df["Classe"] == segmento].groupby("faixa_etaria").agg({"ticket_medio":"mean","valor_monetario":"sum"}).reset_index()
        faixas_etarias = df_agregado["faixa_etaria"].to_list()
        faturamentos = df_agregado["valor_monetario"].to_list()
        fig = go.Figure(go.Bar(x=faixas_etarias,y=faturamentos,orientation="v"))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',
            plot_bgcolor='rgb(17,17,17)',
            yaxis_title=""
        )
        return fig
#--------------------------------------------funcao auxiliar que monta o grafico do ticket medio por faixa etaria----------------------------------------#

def monta_grafico_ticket_medio_faixa_etaria(segmento):
    if segmento is None:
        df_agregado = df.groupby("faixa_etaria").agg({"ticket_medio":"mean","valor_monetario":"sum"}).reset_index()
        faixas_etarias = df_agregado["faixa_etaria"].to_list()
        tickets_medios = df_agregado["ticket_medio"].to_list()
        fig = go.Figure(go.Bar(x=faixas_etarias,y=tickets_medios,orientation="v"))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',
            plot_bgcolor='rgb(17,17,17)',
            yaxis_title=""
        )
        return fig
    else:
        df_agregado = df[df["Classe"] == segmento].groupby("faixa_etaria").agg({"ticket_medio":"mean","valor_monetario":"sum"}).reset_index()
        faixas_etarias = df_agregado["faixa_etaria"].to_list()
        tickets_medios = df_agregado["ticket_medio"].to_list()
        fig = go.Figure(go.Bar(x=faixas_etarias,y=tickets_medios,orientation="v"))
        fig.update_layout(
            paper_bgcolor='rgb(17,17,17)',
            plot_bgcolor='rgb(17,17,17)',
            yaxis_title=""
        )
        return fig
    
#----------------------------------------------------funcao auxiliar que formata a tabela de cluster-----------------------------------------------#

def formata_tabela(df):
    df['Recência'] = df['Recência'].apply(lambda x: x.split(" ")[0])
    df.drop(columns=["nome","nr_cpf_cnpj","Outlier","Frequencia"],axis=1,inplace=True)
    df.rename(columns={"id_cliente":"Id Cliente","faixa_etaria":"Faixa Etária","Classe":"Segmento","cidade":"Cidade","valor_monetario":"Faturamento","ticket_medio":"Ticket Médio","R quintil":"R","F quintil":"F","V quintil":"V"},inplace=True)
         

#-----------------------------------------------------Calculo do faturamento de cada classe--------------------------------------------------------#

dic_faturamento_classe = {}
df_outlier = df[df["Outlier"] == "Sim"]
df_nao_outlier = df[df["Outlier"] == "Não"]
dic_faturamento_classe["Outlier"] = round(df_outlier["valor_monetario"].sum(),2)
for classe in list(df["Classe"].unique()):
    if (classe != " "):
        dic_faturamento_classe[classe] = round(df_nao_outlier[df_nao_outlier["Classe"] == classe]["valor_monetario"].sum(),2)
sorted_faturamento_classe = sorted(dic_faturamento_classe.items(), key=lambda x: x[1], reverse=True)
classes = [item[0] for item in sorted_faturamento_classe]
faturamento = [item[1] for item in sorted_faturamento_classe]
total_faturamento = sum(faturamento)
percentagem_acumulada = [sum(faturamento[:i + 1]) / total_faturamento * 100 for i in range(len(faturamento))]
cores = ["#DC143C","#006400","#4169E1","#FF4500","#800020","#FFDB58","#2E8B57","#F5F5F5","#32CD32"]
fig_grafico = {
    'data': [go.Bar(x=classes, y=faturamento, marker_color=cores),
             go.Scatter(x=classes, y=percentagem_acumulada, yaxis='y2', mode='lines+markers', name='Curva de Pareto', line=dict(color='white'))],
    'layout': {
        'title': 'Faturamento por Classe',
        'yaxis_title': 'Faturamento Total',
        'yaxis2': {'title': 'Porcentagem Acumulada', 'overlaying': 'y', 'side': 'right'},
        'paper_bgcolor': 'rgb(17,17,17)',
        'plot_bgcolor': 'rgb(17,17,17)',
        'font': {'color': 'white'}
    }
}

layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.H2("Analise 360 Segmento",style={"font-size":"25px","color":"#FF8C00"})
                ])
            ],style={"border": "17px solid transparent","background-color":"#000000"}),
            dbc.Row(dbc.Col(style={"border": "14px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id="grafico-faturamento",figure=fig_grafico),
                    dcc.Store(id="guarda-classe",data=None)
                ])
            ]),
            dbc.Row(dbc.Col(style={"border": "10px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([
                    dbc.CardHeader(html.H4("Recência", className="mb-0 text-center",style={"font-size":"18px"}) ),
                    dbc.Card([
                        dbc.CardBody(
                            id="tabela-recencia"
                        )
                    ],style={"background-color":"#000000"})
                ],width=4),
                dbc.Col([
                    dbc.CardHeader(html.H4("Frequência", className="mb-0 text-center",style={"font-size":"18px"}) ),
                    dbc.Card([
                        dbc.CardBody(
                            id="tabela-frequencia"
                        )
                    ],style={"background-color":"#000000"})
                ],width=4),
                dbc.Col([
                    dbc.CardHeader(html.H4("Valor", className="mb-0 text-center",style={"font-size":"18px"}) ),
                    dbc.Card([
                        dbc.CardBody(
                            id="tabela-valor"
                        )
                    ],style={"background-color":"#000000"})
                ],width=4)
            ],className="g-0"),
            dbc.Row([
                dbc.Col([
                    html.H2("Análise de Consumo",style={"font-size":"20px","color":"#FF8C00","text-align":"center"})
                ])
            ],style={"background-color":"#000000"}),
            dbc.Row(dbc.Col(style={"border": "14px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([
                    html.H3("Top setores",style={"font-size":"20px","color":"#FF8C00","text-align":"left"})
                ],width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id="select-top-setores",
                        multi=False,
                        clearable=False,
                        value=3,
                        options=[{"label":x,"value":x} for x in [1,2,3,4,5,6,7]],
                        style={ "margin-left": "0px"}

                    )
                ],width=1),
                dbc.Col([],width=3),
                dbc.Col([
                    html.H3("Top produtos",style={"font-size":"20px","color":"#FF8C00","text-align":"left","padding-left":"2px"})
                ],width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id="select-top-produtos",
                        multi=False,
                        clearable=False,
                        value=3,
                        options=[{"label":x,"value":x} for x in [1,2,3,4,5,6,7,8,9,10]]

                    )
                ],width=1)
            ],style={"background-color":"#000000"},className="g-0"),
            dbc.Row([
                dbc.Col([
                    html.Div(id="tabela-top-setores")
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    html.H2("Análise da Cesta de Compra",style={"font-size":"20px","color":"#FF8C00","text-align":"center"})
                ])
            ],style={"background-color":"#000000"}),
            dbc.Row([
                dbc.Col([
                    html.H4("Confiança",style={"font-size":"15px"})
                ],width=4),
                dbc.Col([
                   dcc.RangeSlider(
                       id="confidence-slider",
                       min=round(menor_confidence,2),
                       max=round(maior_confidence,2),
                       step=None,
                       value=[menor_confidence,maior_confidence]
                   )
                ],width=8)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4("Lift",style={"font-size":"15px"})
                ],width=4),
                dbc.Col([
                    dcc.RangeSlider(
                        id="lift-slider",
                        min=round(menor_lift,2),
                        max=round(maior_lift,2),
                        step=None,
                        value=[menor_lift,maior_lift]
                    )
                ],width=8)
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div(
                        id="regras_associacao_tabela"
                    )
                ])
            ],style={"background-color":"#000000"}),
            dbc.Row(dbc.Col(style={"border": "10px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([
                    html.H3("Faturamento por faixa etaria",id="faixa-etaria-text")
                ],width=5),
                dbc.Col([
                    dcc.Dropdown(
                        id="select_faturamento_ticket_medio",
                        value="Faturamento",
                        options=[{"label":x,"value":x} for x in ["Faturamento","Ticket Médio"]],
                        clearable=False,
                        multi=False
                    )
                ],width=7)
            ],style={"background-color":"#000000"}),
            dbc.Row(dbc.Col(style={"border": "5px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([

                    dcc.Graph(id="faixa_etaria_graficos",figure=monta_grafico_faturamento_faixa_etaria(None)),
                    dcc.Store(id="guarda-faixa-etaria",data=None)
                ])
            ],style={"background-color":"#000000"}),
            dbc.Row(dbc.Col(style={"border": "10px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([
                    html.H2("Cluster de Clientes",style={"font-size":"20px","color":"#FF8C00","text-align":"center"}),
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    html.Button("Download Cluster",id="botao-baixar-tabela"),
                    dcc.Download(id="download-tabela")
                ],style={"text-align":"left"})
            ]),
            dbc.Row(dbc.Col(style={"border": "10px solid transparent","background-color":"#000000"})),
            dbc.Row([
                dbc.Col([
                    html.Div(id="tabela-cluster",style={"background-color":"black"})
                ])
            ])
        ])
    ],style={"border": "17px solid transparent","background-color":"#000000"})
],fluid=True,style={"border": "17px solid transparent","background-color":"#000000"})

#-----------------------------callback para guardar a classe selecionada através do clique no grafico------------------------#

@app.callback(
        Output(component_id="guarda-classe",component_property="data"),
        [Input(component_id="grafico-faturamento",component_property="clickData")]
)

def guarda_classe(click_data):
    if click_data is not None and 'points' in click_data:
        classe_selecionada = click_data['points'][0]['x']
        return classe_selecionada
    else:
        None

#--------------------------------------------callback para destacar no grafico a barra selecionada---------------------------------------------#
        
@app.callback(
        Output(component_id="grafico-faturamento",component_property="figure"),
        [Input(component_id="grafico-faturamento",component_property="clickData")]
)

def destaca_barra_classe(data):
    if data is not None:
        classe_clicada = data['points'][0]['x']
        posicao_classe = classes.index(classe_clicada)
        cores_preto = ["#000000","#000000","#000000","#000000","#000000","#000000","#000000","#000000","#000000"]
        cores_preto[posicao_classe] = 'red'
        fig_destacado = go.Figure(go.Bar(x=classes, y=faturamento, marker_color=cores_preto))
        fig_destacado.update_layout(
            title='Faturamento por Classe',
            yaxis_title='Faturamento Total',
            paper_bgcolor='rgb(17,17,17)',
            plot_bgcolor='rgb(17,17,17)',
            font={'color': 'white'}
        )
        return fig_destacado   
    else:
        return fig_grafico

#-----------------callback para alterar as tabelas de recencia frequencia e valor de acordo com a classe selecionada---------#
        
@app.callback(
        [Output(component_id="tabela-recencia",component_property="children"),
         Output(component_id="tabela-frequencia",component_property="children"),
         Output(component_id="tabela-valor",component_property="children")],
         [Input(component_id="guarda-classe",component_property="data")]
)
def altera_tabelas(data):
    min_r,max_r,min_f,max_f,min_v,max_v = [],[],[],[],[],[]
    if data is None:
        indices = [1,2,3,4,5]
        for i in range(1,6):
            min_r.append(df[df["R quintil"] == i]["Recência"].min())
            max_r.append(df[df["R quintil"] == i]["Recência"].max())
            min_f.append(df[df["F quintil"] == i]["Frequencia"].min())
            max_f.append(df[df["F quintil"] == i]["Frequencia"].max())
            min_v.append(df[df["V quintil"] == i]["valor_monetario"].min())
            max_v.append(df[df["V quintil"] == i]["valor_monetario"].max())
        df_r = pd.DataFrame({"Pontuação R":indices,"Min R":min_r,"Max R":max_r},index=indices)
        df_f = pd.DataFrame({"Pontuação F":indices,"Min F":min_f,"Max F":max_f},index=indices)
        df_v = pd.DataFrame({"Pontuação V":indices,"Min V":min_v,"Max V":max_v},index=indices)
        df_r["Min R"] =df_r["Min R"].apply(lambda x: x.split(' ')[0])
        df_r["Max R"] = df_r["Max R"].apply(lambda x: x.split(' ')[0])
        tabela_recencia = dash_table.DataTable(
            columns=[{"name":col,"id":col} for col in df_r.columns],
            data = df_r.to_dict('records'),
            style_table={ 'font-size': '10px'},
            style_cell={'textAlign': 'center','backgroundColor':'black'}
        )
        tabela_frequencia = dash_table.DataTable(
            columns=[{"name":col,"id":col} for col in df_f.columns],
            data = df_f.to_dict('records'),
            style_table={ 'font-size': '10px'},
            style_cell={'textAlign': 'center','backgroundColor':'black'}
        )
        tabela_valor = dash_table.DataTable(
            columns=[{"name":col,"id":col} for col in df_v.columns],
            data = df_v.to_dict('records'),
            style_table={ 'font-size': '10px'},
            style_cell={'textAlign': 'center','backgroundColor':'black'}
        )
        return [tabela_recencia,tabela_frequencia,tabela_valor]
    else :
        df_filtrado = df[df["Classe"] == data]
        indices_r = []
        indices_f = []
        indices_v = []
        max_val_r = df_filtrado["R quintil"].max()
        min_val_r = df_filtrado["R quintil"].min()
        max_val_f = df_filtrado["F quintil"].max()
        min_val_f = df_filtrado["F quintil"].min()
        max_val_v = df_filtrado["V quintil"].max()
        min_val_v = df_filtrado["V quintil"].min()
        for i in range(min_val_r,max_val_r + 1):
            indices_r.append(i)
            min_r.append(df_filtrado[df_filtrado["R quintil"] == i]["Recência"].min())
            max_r.append(df_filtrado[df_filtrado["R quintil"] == i]["Recência"].max())
        for i in range(min_val_f,max_val_f + 1):
            indices_f.append(i)
            min_f.append(df_filtrado[df_filtrado["F quintil"] == i]["Frequencia"].min())
            max_f.append(df_filtrado[df_filtrado["R quintil"] == i]["Frequencia"].max())
        for i in range(min_val_v,max_val_v + 1):
            indices_v.append(i)
            min_v.append(df_filtrado[df_filtrado["V quintil"] == i]["valor_monetario"].min())
            max_v.append(df_filtrado[df_filtrado["V quintil"] == i]["valor_monetario"].max())
        df_r = pd.DataFrame({"Pontuação R":indices_r,"Min R":min_r,"Max R":max_r},index=indices_r)
        df_f = pd.DataFrame({"Pontuação F":indices_f,"Min F":min_f,"Max F":max_f},index=indices_f)
        df_v = pd.DataFrame({"Pontuação V":indices_v,"Min V":min_v,"Max V":max_v},index=indices_v)
        df_r["Min R"] =df_r["Min R"].apply(lambda x: x.split(' ')[0])
        df_r["Max R"] = df_r["Max R"].apply(lambda x: x.split(' ')[0])
        tabela_recencia = dash_table.DataTable(
            columns=[{"name":col,"id":col} for col in df_r.columns],
            data = df_r.to_dict('records'),
            style_table={ 'font-size': '10px'},
            style_cell={'textAlign': 'center','backgroundColor':'black'}
        )
        tabela_frequencia = dash_table.DataTable(
            columns=[{"name":col,"id":col} for col in df_f.columns],
            data = df_f.to_dict('records'),
            style_table={ 'font-size': '10px'},
            style_cell={'textAlign': 'center','backgroundColor':'black'}
        )
        tabela_valor = dash_table.DataTable(
            columns=[{"name":col,"id":col} for col in df_v.columns],
            data = df_v.to_dict('records'),
            style_table={ 'font-size': '10px'},
            style_cell={'textAlign': 'center','backgroundColor':'black'}
        )
        return [tabela_recencia,tabela_frequencia,tabela_valor]

#-------------------------------------------------callback para montar a analise de consumo----------------------------------------#

@app.callback(
    Output(component_id="tabela-top-setores",component_property="children"),
    [Input(component_id="select-top-setores",component_property="value"),
     Input(component_id="select-top-produtos",component_property="value"),
     Input(component_id="guarda-classe",component_property="data")]
)

def monta_tabela(top_setores,top_produtos,classe):
    print(top_produtos)
    print(top_setores)
    children = []
    for i in range(top_setores):
        colunas = []
        if (i == 0):
            colunas.append(
                dbc.Col([
                    dbc.Card([
                       dbc.CardHeader(html.H4("Top setores",style={"font-size":"10px"}),style={"background-color":"#000000"}),
                       dbc.CardBody([
                           html.H4(f'{i + 1}')
                       ],style={"background-color":"#000000"})
                   ],style={"background-color":"#000000"})
                ],width=1))
            colunas.append(dbc.Col([
                    dbc.Card([
                        dbc.CardHeader(html.H4("Setor",style={"font-size":"10px"}),style={"background-color":"#000000"}),
                        dbc.CardBody(children=monta_card_nome_segmento(i,classe),style={"background-color":"#000000"})                      
                    ],style={"background-color":"#000000"})
                    
                ],width=1))
            colunas.append(dbc.Col([
                   dbc.Card([
                       dbc.CardHeader(html.H4("Top produtos",style={"font-size":"10px"}),style={"background-color":"#000000"}),
                       dbc.CardBody(children = monta_card_qnt_top_produtos(top_produtos))
                   ],style={"background-color":"#000000"})
                ],width=1)),
            colunas.append(dbc.Col([
                   dbc.Card([
                       dbc.CardHeader(html.H4("Produto",style={"font-size":"10px"}),style={"background-color":"#000000"}),
                       dbc.CardBody(children = monta_card_top_produtos(top_produtos,top_7_setores[i],classe)
                       )
                   ],style={"background-color":"#000000"})
                ],width=3))
            colunas.append(dbc.Col([
                    dbc.Card([
                        dbc.CardHeader(html.H4("Faturamento por produto",style={"font-size":"10px"}),style={"background-color":"#000000"}),
                        dbc.CardBody([
                            dcc.Graph(figure=monta_card_grafico(top_produtos,top_7_setores[i],i,classe))
                        ])
                    ],style={"background-color":"#000000"})
                ],width=6))
        else:
            colunas.append(
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                           html.H4(f'{i + 1}')
                       ],style={"background-color":"#000000"})
                   ],style={"background-color":"#000000"})
               ],width=1))
            colunas.append(dbc.Col([
                    dbc.Card([
                        dbc.CardBody(children=monta_card_nome_segmento(i,classe),style={"background-color":"#000000"})
                   ],style={"background-color":"#000000"})
               ],width=1)),
            colunas.append(dbc.Col([
                    dbc.Card([
                        dbc.CardBody(children=monta_card_qnt_top_produtos(top_produtos),style={"background-color":"#000000"}
                       )
                   ],style={"background-color":"#000000"})
               ],width=1)),
            colunas.append(dbc.Col([
                    dbc.Card([
                        dbc.CardBody(children=monta_card_top_produtos(top_produtos,top_7_setores[i],classe),style={"background-color":"#000000"})
                   ],style={"background-color":"#000000"})
               ],width=3)),
            colunas.append(dbc.Col([
                   dbc.Card([
                       dbc.CardBody([
                           dcc.Graph(figure=monta_card_grafico(top_produtos,top_7_setores[i],i,classe))
                       ],style={"background-color":"#000000"})
                   ],style={"background-color":"#000000"})
               ],width=6))
           
        linha = dbc.Row(children=colunas, style={"background-color": "#000000"},className="g-0")
        children.append(linha)
    return children
        
#--------------------------------------callback do grafico de faturamento/ticket médio por faixa etária---------------------------------------------------------#
    
@app.callback(
    [Output(component_id="faixa-etaria-text",component_property="children"),
     Output(component_id="faixa_etaria_graficos",component_property="figure")],
     [Input(component_id="select_faturamento_ticket_medio",component_property="value"),
      Input(component_id="guarda-classe",component_property="data")]
)

def monta_grafico(x,classe):
    if x == "Faturamento":
        return "Faturamento por faixa etaria",monta_grafico_faturamento_faixa_etaria(classe)
    elif x == "Ticket Médio":
        return "Ticket Médio por faixa etaria",monta_grafico_ticket_medio_faixa_etaria(classe)
    
#--------------------------------------------------callback para salvar a faixa etária selecioada---------------------------------------------------------------#
    
@app.callback(
        Output(component_id="guarda-faixa-etaria",component_property="data"),
        [Input(component_id="faixa_etaria_graficos",component_property="clickData")]
)

def guarda_faixa_etaria(click_data):
    if click_data is not None and 'points' in click_data:
        faixa_selecionada = click_data['points'][0]['x']
        return faixa_selecionada
    else:
        None

#---------------------------------callback da analise da cesta de compras-----------------------------------------------------#
        
@app.callback(
    Output(component_id="regras_associacao_tabela",component_property="children"),
    [Input(component_id="confidence-slider",component_property="value"),
     Input(component_id="lift-slider",component_property="value")]
)

def monta_tabela_regras_associacao(valores_confianca,valores_lift):
    menor_confianca,maior_confianca = valores_confianca
    menor_lift,maior_lift = valores_lift
    maior_confianca = round(maior_confianca,2)
    menor_confianca = round(menor_confianca,2)
    maior_lift = round(maior_lift,2)
    menor_lift =  round(menor_lift,2)
    df_filtrado = df_regras_associacao[(df_regras_associacao["confidence"] < maior_confianca) & (df_regras_associacao["confidence"] > menor_confianca) & (df_regras_associacao["lift"]< maior_lift) & (df_regras_associacao["lift"] > menor_lift)]
    df_filtrado.rename(columns={
        "antecedent":"Antecedente",
        "consequent":"Consequente",
        "confidence":"Confiança",
        "lift":"Lift",
        "support":"Suporte"
    },inplace=True)
    styles = [
        {'if':{"column_id":"Confiança"},"color":"#00CED1"},
        {"if":{"column_id":"Suporte"},"color":"#FF4500"},
        {"if":{"column_id":"Lift"},"color":"red"}
    ]
    df_filtrado["Antecedente"] = df_filtrado["Antecedente"].apply(lambda x:x[0])
    df_filtrado["Consequente"] = df_filtrado["Consequente"].apply(lambda x:x[0])
    children = [dash_table.DataTable(
        columns=[{"name":col,"id":col} for col in df_filtrado.columns],
        data=df_filtrado.to_dict('records'),
        style_data_conditional=styles,
        style_table={ 'font-size': '14px'},
        style_cell={'textAlign': 'center','backgroundColor':'black'}
    )]
    return children

#-------------------------------------------------callback para montar a tabela com o cluster correspondente---------------------------------------------------#

@app.callback(
    Output(component_id="tabela-cluster",component_property="children"),
    [Input(component_id="guarda-classe",component_property="data"),
     Input(component_id="guarda-faixa-etaria",component_property="data")]
)

def monta_tabela(classe,faixa_etaria):
    if (classe is None) and (faixa_etaria is None):
        df_top_10 = df.head(10)
        formata_tabela(df_top_10)
        children = [
            dbc.Table.from_dataframe(df_top_10,hover=True,bordered=True,striped=True,style={"font-size":"12px"})
        ]
        return children
    elif (classe is None) and (faixa_etaria is not None):
        df_filtrado = df[df["faixa_etaria"] == faixa_etaria]
        df_top_10 = df_filtrado.head(10)
        formata_tabela(df_top_10)
        children = [
            dbc.Table.from_dataframe(df_top_10,hover=True,bordered=True,striped=True,style={"font-size":"12px"})
        ]
        return children
    elif (classe is not None) and (faixa_etaria is None):
        df_filtrado = df[df["Classe"] == classe]
        df_top_10 = df_filtrado.head(10)
        formata_tabela(df_top_10)
        children = [
            dbc.Table.from_dataframe(df_top_10,hover=True,bordered=True,striped=True,style={"font-size":"12px"})
        ]
        return children
    else :
        df_filtrado = df[(df["Classe"] == classe) & (df["faixa_etaria"] == faixa_etaria)]
        df_top_10 = df_filtrado.head(10)
        formata_tabela(df_top_10)
        children = [
            dbc.Table.from_dataframe(df_top_10,hover=True,bordered=True,striped=True,style={"font-size":"12px"})
        ]
        return children

#--------------------------------------------callback para baixar a tabela do cluster------------------------------------------------------------------------#
    
@app.callback(
    Output(component_id="download-tabela",component_property="data"),
    [Input(component_id="botao-baixar-tabela",component_property="n_clicks"),
     Input(component_id="guarda-classe",component_property="data"),
     Input(component_id="guarda-faixa-etaria",component_property="data")],
    prevent_initial_call=True
)

def baixar_tabela(n_clicks,classe,faixa_etaria):
    pasta_download = os.path.expanduser("~/Downloads")
    caminho_completo = os.path.join(pasta_download,"cluster.csv")
    if n_clicks is None:
        pass
    else:
        if (classe is None) and (faixa_etaria is None):
            df.to_csv(caminho_completo,index=False)
            return dcc.send_file(caminho_completo)
        elif (classe is not None) and (faixa_etaria is None):
            df_filtrado = df[df["Classe"] == classe]
            df_filtrado.to_csv(caminho_completo,index=False)
            return dcc.send_file(caminho_completo)
        elif (classe is None) and (faixa_etaria is not None):
            df_filtrado = df[df["faixa_etaria"] == faixa_etaria]
            df_filtrado.to_csv(caminho_completo,index=False)
            return dcc.send_file(caminho_completo)
        else:
            df_filtrado = df[(df["Classe"] == classe) & (df["faixa_etaria"] == faixa_etaria)]
            df_filtrado.to_csv(caminho_completo,index=False)
            return dcc.send_file(caminho_completo)
#if __name__ == "__main__":
    #app.run_server(debug=True)


