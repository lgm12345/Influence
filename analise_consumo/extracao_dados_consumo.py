import pandas as pd
import mysql.connector
from mysql.connector import Error

#---------------------------------------------Conexão com o banco de dados-----------------------------------------------------#

connection = mysql.connector.connect(
    host="192.168.33.216",
    user="bi",
    passwd="Bi#2020#",
    db="bidb",
    port="3306"
)
#----------------------------------------------Extracao dados analise de consumo geral----------------------------------------#
cursor = connection.cursor()
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = "/home/lucas/anaconda3/Influence/dados/analise_consumo.csv"
destino_top_setores = "/home/lucas/anaconda3/Influence/dados/top_setores.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#----------------------------------------------Extraçao dados analise de consumo setor Campeao--------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Campeao' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = f"/home/lucas/anaconda3/Influence/dados/analise_consumo_campeao.csv"
destino_top_setores = f"/home/lucas/anaconda3/Influence/dados/top_setores_campeao.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#---------------------------------------------Extracao dados analise de consumo setor Valioso---------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Valioso' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = f"/home/lucas/anaconda3/Influence/dados/analise_consumo_valioso.csv"
destino_top_setores = f"/home/lucas/anaconda3/Influence/dados/top_setores_valioso.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#---------------------------------------------Extracao dados analise de consumo setor Cliente Novo---------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Cliente Novo' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = f"/home/lucas/anaconda3/Influence/dados/analise_consumo_cliente_novo.csv"
destino_top_setores = f"/home/lucas/anaconda3/Influence/dados/top_setores_cliente_novo.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#-----------------------------------------------Extracao dados analise consumo setor Incerto----------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Incerto' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = f"/home/lucas/anaconda3/Influence/dados/analise_consumo_incerto.csv"
destino_top_setores = f"/home/lucas/anaconda3/Influence/dados/top_setores_incerto.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#-------------------------------------------------Extracao dados analise consumo setor Em Risco-----------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Em Risco' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = "/home/lucas/anaconda3/Influence/dados/analise_consumo_em_risco.csv"
destino_top_setores = "/home/lucas/anaconda3/Influence/dados/top_setores_em_risco.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#--------------------------------------------------Extracao dados consumo setor Outlier--------------------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Outlier' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
print("3")
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = "/home/lucas/anaconda3/Influence/dados/analise_consumo_outlier.csv"
destino_top_setores = "/home/lucas/anaconda3/Influence/dados/top_setores_outlier.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#-------------------------------------------------Extracao dados consumo setor Nao Perder--------------------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Nao Perder' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = "/home/lucas/anaconda3/Influence/dados/analise_consumo_nao_perder.csv"
destino_top_setores = "/home/lucas/anaconda3/Influence/dados/top_setores_nao_perder.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#-------------------------------------------------Extracao dados consumo setor Adormecido----------------------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Adormecido' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = "/home/lucas/anaconda3/Influence/dados/analise_consumo_adormecido.csv"
destino_top_setores = "/home/lucas/anaconda3/Influence/dados/top_setores_adormecido.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")
#-------------------------------------------------Extracao dados consumo setor Promissor-----------------------------------------------------#
query = "select dim_produto.nm_produto,dim_produto.ds_classe2,sum(fato_venda.vl_total) FROM dim_produto JOIN fato_venda on dim_produto.id_produto = fato_venda.id_produto JOIN dim_cliente on fato_venda.id_cliente = dim_cliente.id_cliente WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and dim_cliente.nm_segmento = 'Promissor' and fato_venda.cd_data BETWEEN '20190101' and '20190131' GROUP BY dim_produto.ds_classe2,dim_produto.nm_produto"
cursor.execute(query)
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["nm_produto","ds_classe2","vl_total"])
df_setores = df.groupby("ds_classe2")["vl_total"].sum().sort_values(ascending=False)
df_setores = df_setores.reset_index()
df_setores.columns = ["ds_classe2","vl_total"]
destino_analise_consumo = "/home/lucas/anaconda3/Influence/dados/analise_consumo_promissor.csv"
destino_top_setores = "/home/lucas/anaconda3/Influence/dados/top_setores_promissor.csv"
df.to_csv(destino_analise_consumo,mode="w")
df_setores.to_csv(destino_top_setores,mode="w")