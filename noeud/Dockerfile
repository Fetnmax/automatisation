FROM postgres:latest
LABEL version="1.0" maintainer="Laborde Romain r.laborde@etud.univ-pau.fr"
COPY data.sql /docker-entrypoint-initdb.d/
ENV POSTGRES_USER test
ENV POSTGRES_PASSWORD toto 
ENV POSTGRES_DB WPAGE
EXPOSE 5432
