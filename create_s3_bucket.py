#Importação da boto3
import boto3 

#Determinação do client 
s3_client = boto3.client("s3")
#Parâmetros não especificados, visto que foram utilizados os já configurados 

#Variável para armazenar o nome do bucket a ser criado 
bucket_name = "teste-bucket-s3-curso-udemy"
#Não pode existir dois buckets com o mesmo nome na mesma região 

#Variável para criar de fato o bucket e armazenar o resultado da criação 
response = s3_client.create_bucket(
    Bucket = bucket_name
)
#Bucket = nome do bucket, já determinado na variável "bucket_name" acima 

#Impressão da mensagem de status com o nome do bucket 
print(f"Bucket {bucket_name} criado com sucesso!")


