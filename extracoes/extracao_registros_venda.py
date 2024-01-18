import mysql
from mysql.connector import Error
import pandas as pd


connection = mysql.connector.connect(
    host="192.168.33.216",
    user="bi",
    passwd="Bi#2020#",
    db="bidb",
    port="3306",
)
cursor = connection.cursor()
print("inicio extração")
cursor.execute("select dim_produto.id_produto,dim_produto.nm_produto,dim_produto.ds_classe2,dim_produto.ds_classe3,fato_venda.id_transacao,fato_venda.vl_total,fato_venda.cd_data FROM dim_produto JOIN fato_venda ON dim_produto.id_produto = fato_venda.id_produto WHERE (dim_produto.ds_classe1 = 'Pereciveis' or dim_produto.ds_classe1 = 'Mercearia') and dim_produto.ds_classe2 not in ('Frutas & Hortalicas') and fato_venda.cd_data BETWEEN 20190101 and 20190230")
dados = cursor.fetchall()
print("fim extracao")
df = pd.DataFrame(dados,columns=["id_produto","nm_produto","ds_classe2","ds_classe3","id_venda","vl_total","cd_data"])
df = df.drop_duplicates(subset=["id_venda","nm_produto"])
destino_fato_venda = "/home/lucas/anaconda3/Influence/dados/fato_venda.parquet"
df.to_parquet(destino_fato_venda)

