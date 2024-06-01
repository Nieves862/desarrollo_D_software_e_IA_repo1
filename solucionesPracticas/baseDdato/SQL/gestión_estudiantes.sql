create database gestión_estudiante;

use gestión_estudiante;

show tables;

create table Estudiante (
	ID_ESTUDIANTE int auto_increment,
    Año varchar (30),
    Apellido varchar(20) NOT NULL,
    Nombre varchar(15) NOT NULL,
    E_mail varchar (40) unique,
	DNI int (8) NOT NULL,
	Fecha_De_Nacimiento date NOT NULL,
    Edad int (2) NOT NULL,
    Teléfono int (25),
    Direccion varchar (30),
    Localidad varchar (20),
    Provincia varchar (15),
    primary key (ID_ESTUDIANTE)    
);
-----------------------------------------------------------------------------
create table Materia (
	ID_MATERIA int auto_increment,
	Espacio varchar (25) NOT NULL,
	Profesor varchar (25) NOT NULL,
	Detalle TEXT,
	Carga_Horaria integer NOT NULL,
    primary key (ID_MATERIA)  
);
-----------------------------------------------------------------------------
create table Nota_Formativa (
ID_NOTA_Formativa int auto_increment PRIMARY KEY,
ID_ESTUDIANTE INT NOT NULL,
ID_MATERIA INT NOT NULL,
Nota INT (2),
Fecha_Exámen DATE NOT NULL,
Tipo_Exámen ENUM ('Recuperatorio','Final') NOT NULL,
FOREIGN KEY (ID_ESTUDIANTE) REFERENCES estudiante (ID_ESTUDIANTE),
FOREIGN KEY (ID_MATERIA) REFERENCES materia (ID_MATERIA)
);
-------------------------------------------------------------------------------
CREATE TABLE Asistencia (
  ID_ASISTENCIA INT PRIMARY KEY AUTO_INCREMENT,
  ID_ESTUDIANTE INT NOT NULL,
  ID_MATERIA INT NOT NULL,
  Fecha_Clase DATE NOT NULL,
  Asistencia ENUM('Presente', 'Ausente') NOT NULL,
  Justificacion TEXT,
  FOREIGN KEY (ID_ESTUDIANTE) REFERENCES estudiante(ID_ESTUDIANTE),
  FOREIGN KEY (ID_MATERIA) REFERENCES materia(ID_MATERIA)
);
----------------------------------------------------------------------------------
CREATE TABLE Grupo (
  ID_GRUPO INT PRIMARY KEY AUTO_INCREMENT,
  Nombre_Grupo VARCHAR(50) NOT NULL,
  Año INT NOT NULL,
  FOREIGN KEY (ID_GRUPO) REFERENCES estudiante(ID_ESTUDIANTE)
);


















insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('RINCON', 'Avril', '49223074', '2009/04/16','15', 'Rio Negro', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('GALAN', 'Candelaria', '49223069', '2009/03/27','15', 'Zona Rural', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('LURASCHI', 'Tiara', '48669838', '2008/11/19','15', 'Argentina', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('MERCADO', 'Matias', '48469838', '2008/11/12','15', 'Independencia', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('ARREGUI', 'Agustina', '48452855', '2008/07/10','15', 'Intendente Penna', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('ZARATE', 'Jazmín', '49223080', '2009/04/09','15', 'Argentina', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('CARRIZO', 'Agustina', '49223056', '2009/01/19','15', 'Argentina', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia)  
values ('ZARATE', 'Alexis', '48452856', '2008/10/16','15', 'Necochea', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('MAGNOTTI', 'Corina', '47668172', '2008/08/01','16', 'Entrada', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('PERALTA', 'Antonella', '48452879', '2008/09/24','15', 'Perú', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('MARTINEZ', 'Tiago', '48452878', '2008/10/24','15', 'Bv_Mariano Maldonado', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('ALTAMIRA', 'Jonás', '49223078', '2009/04/21','14', 'Costa Rica', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('ESCOBAR', 'Julieta', '49223082', '2009/05/03','14', 'nosabe', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('ROS', 'Tomas', '48452869', '2008/09/15','15', 'Cordoba', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('CALDERON', 'Romulo', '50926533', '2008/11/22','15', 'Rivera Indarte', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia)  
values ('GALETTO', 'Bautista', '48452887', '2008/10/10','15', 'Congreso Corrientes', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('CASTAGNOVIZ', 'Magdalena', '48452856', '2008/07/15','15', 'Tucumán', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('PEREYRA', 'Felipe', '48452841', '2008/04/30','16', 'Indpendencia', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('QUINTEROS', 'Candela', '49017754', '2008/09/15','15', 'Pedro Medrano', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('ACUÑA', 'Maximo', '48455253', '2008/07/04','15', 'Rafael Nuñez', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia)  
values ('MONCHIETTI', 'Benjamín', '49223054', '2008/12/19','15', 'Figeroa Alcorta', 'Despeñaderos', 'Cba');

insert into cuarto_año (Apellido, Nombre, DNI, Fecha_De_Nacimiento, Edad, Direccion, Localidad, Provincia) 
values ('BENAVIDEZ', 'Ana', '48452858', '2008/07/23','15', 'Pellegrini', 'Despeñaderos', 'Cba');

select * from cuarto_año; 

select Apellido, Nombre from cuarto_año where Nombre='Candela';

select Apellido, Nombre, Edad from cuarto_año;

select Apellido, Nombre from cuarto_año where Edad <>'15';

#La idea de que no se puedan ejecutar ciertos comandos 'delete' es para evitar borrados masivos 
#de datos que luego no podemos recuperar.

#Tenemos dos soluciones para resolver el problema de los 'delete', la primera es encerrar todo el bloque 
#donde ejecutamos los comandos delete cambiando el esta de la variable 'SQL_SAFE_UPDATES':

#El primer método es cambiar el estado de la variable SQL_SAFE_UPDATES en forma temporal:

set SQL_SAFE_UPDATES=0;
----------------------------------------------------------------------------------------------------------------------
set SQL_SAFE_UPDATES=1;

#Tengamos en cuenta que disponer la variable SQL_SAFE_UPDATES para que los borrados sean solo seguros 
#es muy conveniente cuando hay programadores que recién están comenzando en SQL y hay datos valiosos ya almacenados.

#Podemos saber el estado global de la variable 'SQL_SAFE_UPDATES' mediante la consulta:

select @@sql_safe_updates;

delete from cuarto_año where Apellido = 'MARTINEZ';
delete from cuarto_año where Apellido = 'GALETTO';
delete from cuarto_año where Apellido =  'CASTAGNOVIZ';
delete from cuarto_año where Apellido = 'MONCHIETTI';
delete from cuarto_año where Apellido = 'MERCADO';
delete from cuarto_año where Apellido = 'PERALTA';
delete from cuarto_año where Apellido = 'PEREYRA';
delete from cuarto_año where Apellido = 'ZARATE';
delete from cuarto_año where Apellido = 'ALTAMIRA';
delete from cuarto_año where Apellido = 'QUINTEROS';
delete from cuarto_año where Apellido = 'ACUÑA';
delete from cuarto_año where Apellido = 'CALDERON';
delete from cuarto_año where Apellido = 'ARREGUI';
delete from cuarto_año where Apellido = 'GALAN';

#Para modificar uno o varios datos de uno o varios registros utilizamos "update" (actualizar)

update cuarto_año set Provincia ='Córdoba';

update cuarto_año set Direccion ='Intendente Penna'
where Apellido ='ARREGUI';

update cuarto_año set Direccion ='Bv Mariano Maldonado'
where Apellido ='MARTINEZ';

update cuarto_año set Direccion ='Bv San Martín'
where Apellido ='ESCOBAR';

--------------------------------------------------------------------------------------------------------
drop table if exists cuarto_año;

#Clave Primaria / PRIMARY KEY / PK
#es un campo (o varios) que identifica 1 solo registro (fila) en una tabla.
#Para un valor del campo clave existe solamente 1 registro. Los valores no se repiten ni pueden ser nulos.

#Campo entero con autoincremento.
#Para definir un campo autoincrementable colocamos "auto_increment" luego de la definición del campo al crear la tabla.

select Código, Apellido, Nombre from cuarto_año where Edad ='16';









