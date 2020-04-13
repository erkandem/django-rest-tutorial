FROM postgres:12-alpine
ENV POSTGRES_PASSWORD=postgres
COPY init.sql /docker-entrypoint-initdb.d/

# docker build -f dockerfiles/db/Dockerfile -t djrest_db .
# docker run -p 5433:5432 -v djrest_django_rest_database:/var/lib/postgresql/data djrest_db
