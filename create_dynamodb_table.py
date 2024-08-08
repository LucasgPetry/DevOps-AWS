import boto3 

dynamodb_client = boto3.client("dynamodb")

table_name = "customers"

#Colunas do  db 
table_schema = [
    {
        "AttributeName": "id",
        "AttributeType": "N"
    }, 

    {
        "AttributeName": "email",
        "AttributeType": "S"
    }
]

#Estruturas das colunas e suas chaves 

key_schema = [
    {
        "AttributeName": "id",
        "KeyType": "HASH"
    }, 
#HASH - chave primária 
    {
        "AttributeName": "email",
        "KeyType": "RANGE"
    }
#RANGE - o email vai estar sempre associado a um único id 
]

provisioned_throughput = {
    "ReadCapacityUnits" : 5, 
    "WriteCapacityUnits" : 5
}
#ReadCapacityUnits - quantidade de leituras por segundo
#WriteCapacityUnits - quantidade de registros por segundo 

response = dynamodb_client.create_table(
    TableName = table_name, 
    KeySchema = key_schema,
    AttributeDefinitions = table_schema,
    ProvisionedThroughput = provisioned_throughput
)

print(f"Tabela DynamoDB {table_name} criada com sucesso.")