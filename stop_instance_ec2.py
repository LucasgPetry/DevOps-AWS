import boto3 

ec2_client = boto3.client("ec2", region_name = "us-east-1")

instance_id = ["id_da_instância"]

response = ec2_client.stop_instances(InstanceIds = instance_id, Force = False)

for instance in response["StoppingInstances"]: 
    print(f"A instância {instance["InstanceId"]} foi interrompida com sucesso")

