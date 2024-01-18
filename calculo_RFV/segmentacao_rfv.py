import pandas as pd
from datetime import datetime,timedelta
import mysql.connector
from mysql.connector import Error
#-------------------------------------------------Conexão e filtragem dos dados------------------------------------------------------------------#


connection = mysql.connector.connect(
    host="192.168.33.216",
    user="bi",
    passwd="Bi#2020#",
    db="bidb",port="3306")
 
try:
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        db = cursor.fetchone()
        print("Você está conectado ao banco de dados: ", db)
except Error as e:
    print("Erro ao conectar ao MySQL", e)


#-------------------------------------------------Filtragem dos dados da dim_cliente-------------------------------------------------------------#
inicio = datetime.now()
print("Inicio extração dados dim_cliente")
cursor.execute("select id_cliente, nr_cpfcnpj, nm_cliente, nm_cidade, ds_faixa_etaria from dim_cliente")
dados = cursor.fetchall()
print("Final extração dados dim_cliente")
df = pd.DataFrame(dados,columns=["id_cliente", "nr_cpf_cnpj", "nome", "cidade","faixa_etaria"])

#-------------------------------------------------Calculo de R,F,V para cada cliente na fato_venda------------------------------------------------#


query = "select nr_cpfcnpj_cliente , max(date(dt_data)),count(distinct id_transacao), ifnull(sum(vl_total),0),ifnull(avg(vl_total),0) from fato_venda group by nr_cpfcnpj_cliente"
print("Inicio calculo RFV")
inicio_calculo_rfv = datetime.now()
cursor.execute(query)
dados = cursor.fetchall()
df1 = pd.DataFrame(dados, columns=['nr_cpf_cnpj', 'Ultima_compra', 'Frequencia', 'valor_monetario',"ticket_medio"])
final_calculo_rfv = datetime.now()
print("Final calculo RFV")
duracao_calculo_rfv = final_calculo_rfv - inicio_calculo_rfv
df1["Ultima_compra"] = pd.to_datetime(df1["Ultima_compra"])
df1["valor_monetario"] = df1["valor_monetario"].astype(float)


#---------------------------------------------------Junção das tabelas--------------------------------------------------------------------------#

df_rfm = pd.merge(df1,df,on='nr_cpf_cnpj',how='left')

#--------------------------------------------------Transformação da coluna ultima compra em Recência---------------------------------------------#

df_rfm["Ultima_compra"] = df_rfm["Ultima_compra"].apply(lambda x: datetime.now() - x)
df_rfm = df_rfm.rename(columns={"Ultima_compra":"Recência"})


#---------------------------------------------------Divisão em quintis dos valores de R F V-------------------------------------------------------#
print("Inicio divisão quintis")
niveis_r = [5,4,3,2,1]
niveis_f= [1,2,3,4,5]
niveis_v= [1,2,3,4,5]
df_rfm["R quintil"] = pd.qcut(df_rfm["Recência"],5,niveis_r)
df_rfm["F quintil"] = pd.qcut(df_rfm["Frequencia"],5,niveis_f)
df_rfm["V quintil"] = pd.qcut(df_rfm["valor_monetario"],5,niveis_v)
print("Final Divisao quintis")


#----------------------------------------------------Calculo dos outliers--------------------------------------------------------------------------#


df_rfm = df_rfm.set_index("id_cliente")
media = df_rfm["valor_monetario"].mean()
desvio_padrao = df_rfm["valor_monetario"].std()
lista_clientes_ids = list(df_rfm.index)
outlier = []
limite_superior = media + (2 * desvio_padrao)
inicio_calculo_outlier = datetime.now()
print("Inicio calculo outliers")
for cliente_id in lista_clientes_ids:
    valor_monetario = df_rfm.loc[cliente_id,"valor_monetario"]
    if (valor_monetario > limite_superior):
        outlier.append("Sim")
    else:
        outlier.append("Não")
final_calculo_outlier = datetime.now()
print("Final calculo outliers")
duracao_calculo_outlier = final_calculo_outlier - inicio_calculo_outlier
df_rfm["Outlier"] = outlier



#------------------------------------------------------Classificação dos clientes----------------------------------------------------------------#

def classificar(df):
    if(df["R quintil"] == 5):
        if(df["F quintil"] == 5):
            if(df["V quintil"] == 5):
                return "Campeão"
            elif(df["V quintil"] == 4):
                return "Campeão"
            elif(df["V quintil"] == 3):
                return "Promissor"
            elif (df["V quintil"] == 2):
                return "Promissor"
            elif(df["V quintil"] == 1):
                return ""
        elif(df["F quintil"] == 4):
            if(df["V quintil"] == 5):
                return "Campeão"
            elif(df["V quintil"] == 4):
                return "Campeão"
            elif(df["V quintil"] == 3):
                return "Promissor"
            elif (df["V quintil"] == 2):
                return "Promissor"
            elif(df["V quintil"] == 1):
                 return "Promissor"
        elif(df["F quintil"] == 3):
            if(df["V quintil"] == 5):
                return "Valioso"
            elif(df["V quintil"] == 4):
                return "Valioso"
            elif(df["V quintil"] == 3):
                return "Cliente Novo"
            elif (df["V quintil"] == 2):
                return "Cliente Novo"
            elif(df["V quintil"] == 1):
                 return "Cliente Novo"
        elif(df["F quintil"] == 2):
            if(df["V quintil"] == 5):
                return "Valioso"
            elif(df["V quintil"] == 4):
                return "Valioso"
            elif(df["V quintil"] == 3):
                return "Cliente Novo"
            elif (df["V quintil"] == 2):
                return "Cliente Novo"
            elif(df["V quintil"] == 1):
                 return "Cliente Novo"
        elif(df["F quintil"] == 1):
            if(df["V quintil"] == 5):
                return "Valioso"
            elif(df["V quintil"] == 4):
                return "Valioso"
            elif(df["V quintil"] == 3):
                return "Cliente Novo"
            elif (df["V quintil"] == 2):
                return "Cliente Novo"
            elif(df["V quintil"] == 1):
                 return "Cliente Novo"
    elif (df["R quintil"] == 4):
        if (df["F quintil"] == 5):
            if(df["V quintil"] == 5):
                return "Campeão"
            elif(df["V quintil"] == 4):
                return "Campeão"
            elif(df["V quintil"] == 3):
                return "Promissor"
            elif (df["V quintil"] == 2):
                return "Promissor"
            elif(df["V quintil"] == 1):
                 return " "
        elif(df["F quintil"] == 4):
            if(df["V quintil"] == 5):
                return "Campeão"
            elif(df["V quintil"] == 4):
                return "Campeão"
            elif(df["V quintil"] == 3):
                return "Promissor"
            elif (df["V quintil"] == 2):
                return "Promissor"
            elif(df["V quintil"] == 1):
                 return "Promissor"
        elif(df["F quintil"] == 3):
            if(df["V quintil"] == 5):
                return "Valioso"
            elif(df["V quintil"] == 4):
                return "Valioso"
            elif(df["V quintil"] == 3):
                return "Cliente Novo"
            elif (df["V quintil"] == 2):
                return "Cliente Novo"
            elif(df["V quintil"] == 1):
                 return "Cliente Novo"
        elif(df["F quintil"] == 2):
            if(df["V quintil"] == 5):
                return "Valioso"
            elif(df["V quintil"] == 4):
                return "Valioso"
            elif(df["V quintil"] == 3):
                return "Cliente Novo"
            elif (df["V quintil"] == 2):
                return "Cliente Novo"
            elif(df["V quintil"] == 1):
                 return "Cliente Novo"
        elif(df["F quintil"] == 1):
            if(df["V quintil"] == 5):
                return "Valioso"
            elif(df["V quintil"] == 4):
                return "Valioso"
            elif(df["V quintil"] == 3):
                return "Cliente Novo"
            elif (df["V quintil"] == 2):
                return "Cliente Novo"
            elif(df["V quintil"] == 1):
                 return "Cliente Novo"
    elif (df["R quintil"] == 3):
        if (df["F quintil"] == 5):
            if(df["V quintil"] == 5):
                return "Em Risco"
            elif(df["V quintil"] == 4):
                return "Em Risco"
            elif(df["V quintil"] == 3):
                return "Adormecido"
            elif (df["V quintil"] == 2):
                return "Adormecido"
            elif(df["V quintil"] == 1):
                 return ""
        elif(df["F quintil"] == 4):
            if(df["V quintil"] == 5):
                return "Em Risco"
            elif(df["V quintil"] == 4):
                return "Em Risco"
            elif(df["V quintil"] == 3):
                return "Adormecido"
            elif (df["V quintil"] == 2):
                return "Adormecido"
            elif(df["V quintil"] == 1):
                 return "Adormecido"
        elif(df["F quintil"] == 3):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
        elif(df["F quintil"] == 2):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
        elif(df["F quintil"] == 1):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
    elif (df["R quintil"] == 2):
        if (df["F quintil"] == 5):
            if(df["V quintil"] == 5):
                return "Em Risco"
            elif(df["V quintil"] == 4):
                return "Em Risco"
            elif(df["V quintil"] == 3):
                return "Adormecido"
            elif (df["V quintil"] == 2):
                return "Adormecido"
            elif(df["V quintil"] == 1):
                 return " "
        elif(df["F quintil"] == 4):
            if(df["V quintil"] == 5):
                return "Em Risco"
            elif(df["V quintil"] == 4):
                return "Em Risco"
            elif(df["V quintil"] == 3):
                return "Adormecido"
            elif (df["V quintil"] == 2):
                return "Adormecido"
            elif(df["V quintil"] == 1):
                 return "Adormecido"
        elif(df["F quintil"] == 3):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
        elif(df["F quintil"] == 2):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
        elif(df["F quintil"] == 1):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
    elif (df["R quintil"] == 1):
        if (df["F quintil"] == 5):
            if(df["V quintil"] == 5):
                return "Em Risco"
            elif(df["V quintil"] == 4):
                return "Em Risco"
            elif(df["V quintil"] == 3):
                return "Adormecido"
            elif (df["V quintil"] == 2):
                return "Adormecido"
            elif(df["V quintil"] == 1):
                 return "Adormecido"
        elif(df["F quintil"] == 4):
            if(df["V quintil"] == 5):
                return "Em Risco"
            elif(df["V quintil"] == 4):
                return "Em Risco"
            elif(df["V quintil"] == 3):
                return "Adormecido"
            elif (df["V quintil"] == 2):
                return "Adormecido"
            elif(df["V quintil"] == 1):
                 return "Adormecido"
        elif(df["F quintil"] == 3):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
        elif(df["F quintil"] == 2):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
        elif(df["F quintil"] == 1):
            if(df["V quintil"] == 5):
                return "Não Perder"
            elif(df["V quintil"] == 4):
                return "Não Perder"
            elif(df["V quintil"] == 3):
                return "Incerto"
            elif (df["V quintil"] == 2):
                return "Incerto"
            elif(df["V quintil"] == 1):
                 return "Incerto"
            
df_rfm['Classe'] = df_rfm.apply(classificar,axis=1)


print(df_rfm.head())
fim = datetime.now()
tempo_de_execucao = fim - inicio
minutos = tempo_de_execucao.total_seconds() // 60
segundos = tempo_de_execucao.total_seconds() % 60
segundos_round = round(segundos,2)
print(f'tempo de execução: {minutos} minutos e {segundos} segundos')
df_rfm.to_csv("tabela_cliente_segmento.csv",mode="w")




