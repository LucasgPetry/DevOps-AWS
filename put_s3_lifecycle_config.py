import boto3

s3_client = boto3.client("s3")

bucket_name = "teste-bucket-s3-curso-udemy"

lifecycle_configuration = {
    "Rules": [
        {
            "ID": "RegraExpiracao",
            "Status": "Enabled",
            "Prefix": "",
            "Expiration": {
                "Days": 30,
            }
        }
    ]
}
#Prefix - caso queira aplicar a regra dentro de uma pasta 
response = s3_client.put_bucket_lifecycle_configuration(
    Bucket=bucket_name,
    LifecycleConfiguration=lifecycle_configuration
)

print(f"Configuração do ciclo de vida do bucket {bucket_name} atualizada com sucesso.")
