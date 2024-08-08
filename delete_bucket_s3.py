import boto3 

s3_client = boto3.client("s3")

bucket_name = "teste-bucket-s3-curso-udemy"

response = s3_client.delete_bucket(
    Bucket = bucket_name
)

print(f"O bucket {bucket_name} foi excluído com sucesso.")
