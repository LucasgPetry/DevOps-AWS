import boto3 

dynamodb_client = boto3.client("dynamodb")

table_name = "customers"

response = dynamodb_client.delete_table(TableName = table_name)

print(response)
print(f"Tabela {table_name} exclída com sucesso")
