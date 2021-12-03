show databases;

#crea base de datos
create database buscados;
use buscados;

#crea tabla
create table datosbuscados (rut varchar(10), nombre varchar(150), apellido varchar(150), antecedentes varchar(150), buscado varchar (2));

#para insertar valores
insert datosbuscados values(1222, 'nose', 'a', 'no', 'no');

#modificar valores
update datosbuscados SET antecedentes = ('Ser muy feo') where rut  = 123456;

#eliminar todos los datos de la persona
delete from datosbuscados where rut = 1222;

#ver la tabla de datosbuscados
select * from datosbuscados;


