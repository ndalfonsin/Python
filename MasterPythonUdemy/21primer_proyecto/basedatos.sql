CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
id   int(25) auto_increment not null,
nombre  varchar(100),
apellidos Varchar(255),
email Varchar(255) not null,
password  Varchar(255) not null,
fecha  date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE note(
id      int(25) auto_increment not null,
usuario_id int(25) not null, 
titulo      Varchar(255) not null,
descripcion MEDIUMTEXT,
fecha   date not null,
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;