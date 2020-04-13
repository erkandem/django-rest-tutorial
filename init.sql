-- every user should have it's own database, which has the same name as the user
CREATE DATABASE django_rest_app;
CREATE ROLE django_rest_app WITH PASSWORD 'halli_galli_mache_ma_hier_net!';

-- set some default which will prevent lookup queries and therefore speed up all queries
-- source https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
ALTER ROLE django_rest_app SET client_encoding TO 'utf8';
ALTER ROLE django_rest_app SET default_transaction_isolation TO 'read committed';
ALTER ROLE django_rest_app SET timezone TO 'UTC';
ALTER ROLE django_rest_app WITH LOGIN;
ALTER ROLE django_rest_app WITH SUPERUSER;

-- grant rights to read, write, ... and so on
GRANT ALL PRIVILEGES ON DATABASE django_rest_app TO django_rest_app;
