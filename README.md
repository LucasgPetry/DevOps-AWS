# DevOps AWS - Boto3 Scripts ☁️🐍

Este repositório contém uma coleção de scripts Python simples e funcionais utilizando a biblioteca **Boto3** (AWS SDK para Python). O objetivo principal é automatizar tarefas básicas de gerenciamento de infraestrutura na AWS, servindo como uma base de referência para operações de DevOps.

## 🚀 Funcionalidades

Os scripts abordam operações essenciais (CRUD) em serviços principais da AWS:

### **Amazon S3**
- Criar novos buckets.
- Listar buckets existentes.
- Remover buckets e objetos.

### **Amazon EC2**
- Criar e instanciar servidores virtuais.
- Listar instâncias ativas e metadados.
- Parar, iniciar ou terminar instâncias.

---

## 📂 Estrutura do Projeto

```bash
.                
├── src/ #scripts python boto3         
└── README.md
```

## 🛠️ Pré-requisitos

Antes de executar os scripts, certifique-se de ter:

1. **Python 3.x** instalado.
2. **AWS CLI** configurado com suas credenciais (`aws configure`).
3. Biblioteca **Boto3** instalada:
   ```bash
   pip install boto3 

## 📂 Como Usar
Clone o repositório: 
 ``` bash
git clone https://github.com/LucasgPetry/DevOps-AWS.git

cd DevOps-AWS
``` 

Execute o script desejado (certifique-se de revisar os nomes de buckets e IDs de instâncias dentro dos arquivos antes de rodar): 

``` bash
python /src/nome_do_script.py
``` 

## 📖 Estrutura do Código
Os scripts seguem um padrão simples:

Client/Resource: Uso de boto3.client ou boto3.resource para interação.

Funções: Encapsulamento de lógicas básicas para reutilização.

Tratamento de exceções: Estruturas simples de try/except para capturar erros comuns de permissão ou recursos inexistentes.

## ⚠️ Aviso Legal
Estes scripts são para fins de estudo e automação básica. Lembre-se de que a criação de recursos na AWS pode gerar custos. Sempre verifique se os recursos foram devidamente removidos após os testes.

Lucas Petry

https://github.com/LucasgPetry