import boto3

ec2_client = boto3.client("ec2")

instance_id = "id_instancia_criada"
new_instance_type = "t2.nano"

try:
    response = ec2_client.modify_instance_attribute(
        InstanceId=instance_id,
        InstanceType={
            "Value":new_instance_type
        }
    )
    print(f"Tipo da instância {instance_id} modificado para {new_instance_type} com sucesso.")
    
except Exception as instance_error:
    print(f"Erro ao modificar o tipo da instância: {instance_error}")