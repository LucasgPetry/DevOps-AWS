import boto3 

ec2_client = boto3.client("ec2")

#Inicialização da variável next token como nula, já que na primeira chamada ela não será necessária 
next_token = None
#Utilizado para recursos com paginação, pegar as próximas páginas de serviços quando há muitos recursos 

#Criação de um loop infinito
#Se o next_token existir, faça um describe utilizando ele para a paginação 
#Caso não exista, faça normal  
while True: 
    if next_token: 
        response = ec2_client.describe_instance(NextToken=next_token) 
    else: 
        response = ec2_client.describe_insstance()

#Extraindo informações do response para imprimir na listagem    
#Passagem de lista, já que o response é impresso em forma de lista 
    for reservation in response["Reservations"]: 
        for instance in reservation["Instances"]: 
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            state = instance["State"]["Name"]
            print(f"Instance Id: {instance_id}\n Instance Type: {instance_type}\n Instance State: {state} ")

#NextToken antes inicializado como none, agora armazena o valor do NextToken de fato contido no response 
    next_token = response.get("NextToken")

#Se o NextToken não existe, break the program 
    if not next_token: 
        break 