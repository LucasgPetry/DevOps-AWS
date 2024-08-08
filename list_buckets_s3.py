#Importação do boto3
import boto3 

#Determinação do client
s3_client = boto3.client("s3")

#Chamando a função 
response = s3_client.list_buckets()

#Loop para pegar todos os  buckets que estiverem armazenados no response 
for bucket in response["Buckets"]:
    print(f"Bucket: {bucket["Name"]}")
