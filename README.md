# Django-Django-Rest-Framework

## extend user model


### settiing up postgres user.

 sudo su - postgres
 psql


 CREATE ROLE poll_world WITH LOGIN PASSWORD 'poll_world';
 CREATE DATABASE poll_world;
 ALTER USER poll_world WITH SUPERUSER;

 GRANT ALL PRIVILEGES ON DATABASE poll_world TO poll_world;
 ALTER USER poll_world CREATEDB;
