import boto3 

ec2_client = boto3.client("ec2")

instance_id = ["id_da_instância"] 
#Criada em forma de lista caso queira adicionar várias e encerrar todas de forma automatizada com um get 

response = ec2_client.terminate_instances(InstancesIds=instance_id)

print(f"Instância {instance_id} encerrada com sucesso.")

