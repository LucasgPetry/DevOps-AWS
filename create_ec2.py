#Importação do boto3  
import boto3 

#Criação do client, conexão com a AWS para iniciar o serviço. 
ec2_client = boto3.client("ec2", region_name="us-east-1")
#Parâmetro "region_name" utilizado opicionalmente para determinar em qual região tal instância será criada

'''
Outros parâmetros podem ser utilizados caso queira fazer a configuração e a criação da instância em outro 
servidor como o aws_access_key_id e o aws_secret_access_key_id, não especificados vistos que já foram 
configurados.   
'''
#Variável para armazenar o tipo de instância que será criada 
instance_type = "t2.micro"

#Variável para armazenar a imagem/sistema operacional que a instância vai ter por meio do id 
ami_id = "ami-04e5276ebb8451442" 

#Variável para criar de fato a instância e retornar o status da execução do serviço posteriormente
response = ec2_client.run_instances(
    ImageId = ami_id,
    InstanceType = instance_type, 
    MinCount = 1,
    MaxCount = 1
)
#ImageId = imagem utilizada pela instância determinada pela variável "ami_id"
#InstanceType = tipo de instância determinada na variável "instance_type"
#MinCount = Mínimo de instâncias a serem criadas 
#MaxCount = Máximo de instâncias a serem criadas 

#Variável para obter o id da instância criada  
instance_id = response["Instances"][0]["InstanceId"]
#Primeiro elemento da classe "Instances", no caso a única instância criada, com seu respectivo Id  

#Impressão da mensagem do resultado com o id da instância
print(f"Instância de id {instance_id} criada com sucesso!")