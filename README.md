# Django-Django-Rest-Framework

## extend user model


### settiing up postgres user.

 sudo su - postgres
 psql


 CREATE ROLE saleor WITH LOGIN PASSWORD 'saleor';
 CREATE DATABASE saleor;
 ALTER USER saleor WITH SUPERUSER;

 GRANT ALL PRIVILEGES ON DATABASE saleor TO saleor;
 ALTER USER saleor CREATEDB;
