import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="192.168.33.216",
    user ="bi",
    passwd="Bi#2020#",
    db="bidb",
    port="3306"
)
cursor = connection.cursor()
cursor.execute("select id_cliente,dt_data,vl_total from fato_venda where cd_data between '20190301' and '20190304'")
dados = cursor.fetchall()
df = pd.DataFrame(dados,columns=["id_cliente","data","valor"])
destino = "/home/lucas/anaconda3/Influence/dados/dados_cliente_por_venda.parquet"
df.to_parquet(destino)
