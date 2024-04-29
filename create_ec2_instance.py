#Creating a EC2 instance in AWS 
import boto3 

ec2_client = boto3.client("ec2", region_name="us-east-1")

instance_type = "t2.micro"

ami_id = "ami-04e5276ebb8451442" 

response = ec2_client.run_instances(
    ImageId = ami_id,
    InstanceType = instance_type, 
    MinCount = 1,
    MaxCount = 1
)

instance_id = response["Instances"][0]["InstanceId"]

print(f"Instância de id {instance_id} criada com sucesso!")