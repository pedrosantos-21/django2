#Usa uma imagem base Python
FROM python:3.10-slim-buster

#Define o diretório de trabalho dentro do container
WORKDIR /app

#Copia o arquivo requiremnts.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências de sistema necessárias para o mysqlclient
# O --no-install-recommends ajuda a manter a imagem menor
#pkgconf (que fornece pkg-config) e libc6-dev para compiladores C
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc pkgconf libc6-dev \
    && rm -rf /var/lib/apt/lists/*

#Instala as dependências do projeto(Python)
RUN pip install --no-cache-dir -r requirements.txt

#Copia o restante dos arquivos do projeto para o diretório de trabalho
#"Copie tudo que está no diretório atual do meu host (o contexto de build) para o diretório de trabalho atual dentro do contêiner."
COPY . .

#Define a porta que a sua aplcação Djnago irá rodar
#A porta 8000 é a porta padrão do servidor de desenvolvimento do Django
EXPOSE 8000

# Comando para rodar a aplicação Djnago quando o contêiner for iniciado
#Subistituir 'django2.settings' pelo caminho completo do settings.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]