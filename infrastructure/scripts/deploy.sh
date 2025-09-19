#!/bin/bash

# Script de deploy para AWS
set -e

PROJECT_NAME="contai-finance"
AWS_REGION="us-east-1"

echo "🚀 Iniciando deploy do ContAI Finance na AWS..."

# 1. Inicializa Terraform
echo "📋 Inicializando Terraform..."
terraform init

# 2. Planeja infraestrutura
echo "📊 Planejando infraestrutura..."
terraform plan -var="project_name=$PROJECT_NAME" -var="aws_region=$AWS_REGION"

# 3. Aplica infraestrutura
echo "🏗️ Criando infraestrutura..."
terraform apply -auto-approve -var="project_name=$PROJECT_NAME" -var="aws_region=$AWS_REGION"

# 4. Obtém outputs
ECR_REPO=$(terraform output -raw ecr_repository_url)
CLUSTER_NAME=$(terraform output -raw ecs_cluster_name)
ALB_DNS=$(terraform output -raw load_balancer_dns)

echo "📦 ECR Repository: $ECR_REPO"
echo "🎯 ECS Cluster: $CLUSTER_NAME"
echo "🌐 Load Balancer: $ALB_DNS"

# 5. Build e push da imagem Docker
echo "🐳 Construindo imagem Docker..."
cd ..
docker build -t $PROJECT_NAME .

# 6. Tag e push para ECR
echo "📤 Enviando imagem para ECR..."
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_REPO
docker tag $PROJECT_NAME:latest $ECR_REPO:latest
docker push $ECR_REPO:latest

# 7. Atualiza serviço ECS
echo "🔄 Atualizando serviço ECS..."
aws ecs update-service --cluster $CLUSTER_NAME --service ${PROJECT_NAME}-service --force-new-deployment --region $AWS_REGION

echo "✅ Deploy concluído!"
echo "🌐 Aplicação disponível em: http://$ALB_DNS"
echo ""
echo "📋 Próximos passos:"
echo "1. Aguarde alguns minutos para o serviço ficar disponível"
echo "2. Acesse a aplicação no endereço acima"
echo "3. Faça upload de um arquivo CSV para testar"
echo "4. Use o chat para fazer perguntas sobre os dados"