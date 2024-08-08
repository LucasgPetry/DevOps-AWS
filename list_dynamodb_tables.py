#Importação do boto3 
import boto3 

#Criação do client 
dynamodb_client = boto3.client("dynamodb")

#Criação do paginator para retornar todas as páginas sem precisar do token 
paginator = dynamodb_client.get_paginator("list_tables")
#Argumento do get_paginator = função que deseja paginar 

#Loop para pegar cada table_name dentro da paginação realizada 
for page in paginator.paginate():
    for table_name in page["TableNames"]:
        print(f"Table: {table_name}")