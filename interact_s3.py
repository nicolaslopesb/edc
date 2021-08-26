import boto3
import pandas as pd 

# Criar um cliente para interagir com o AWS S3. 
s3_client = boto3.client('s3')

s3_client.download_file("datalake-nico",
                        "data/alimentadores.csv", 
                        "data/alimentadores.csv")

df = pd.read_csv('data/alimentadores.csv')
print(df)

s3_client.upload_file('data/folha_presenca.csv',
                    'datalake-nico',
                    'data/folha_presenca_up.csv')