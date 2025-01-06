# Basé sur l'image Jenkins agent officielle
FROM jenkins/agent:latest

# Passer à l'utilisateur root pour installer des paquets
USER root

# Installer Python et pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

# Revenir à l'utilisateur Jenkins pour des raisons de sécurité
USER jenkins
