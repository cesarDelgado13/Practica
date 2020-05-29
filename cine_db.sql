CREATE DATABASE  IF NOT exists cine;

use cine;

create table if not exists users(

	id_user int not null auto_increment,
	nombre varchar(60) not null,
    email varchar(40) not null,
    phone varchar(13) not null,
    
    primary key(id_user)
    
)engine = InnoDB;

create table if not exists administrador(

	id_admin int not null auto_increment,
    nombre varchar(60) not null,
    posicion varchar(20) not null,
    pass varchar(30),
    
    primary key(id_admin)

)engine = InnoDB;

create table if not exists ticket(

    id_ticket int not null auto_increment,
    total_asientos int not null,
    total_pago int not null,
    
    primary key(id_ticket)

)engine = InnoDB;

create table if not exists sala(

	no_sala int not null,
    capacidad int not null,
    tipo enum('VIP', 'Normal', '3D'),
    
    primary key(no_sala)

)engine = InnoDB;

create table if not exists detalles_asiento(

    id_user int not null,
    no_sala int not null,
    id_ticket int not null,
    asiento enum('libre','ocupado','apartado'),
    
    primary key(no_sala, id_user),
    
    constraint fkdetalles_users foreign key (id_user)
		references users(id_user)
        on delete cascade
        on update cascade,
        
	constraint fkdetalles_sala foreign key (no_sala)
		references sala(no_sala)
        on delete cascade
        on update cascade,
        
	constraint fkdetalles_ticket foreign key (id_ticket)
		references ticket(id_ticket)
        on delete cascade
        on update cascade

)engine = InnoDB;

create table if not exists horario(

	id_horario date not null,
    id_admin int not null,
    estrenos varchar(60),
    preestrenos varchar(60),
    especiales varchar(60),
    
    primary key(id_horario),
    
    constraint fk_horario foreign key (id_admin)
		references administrador(id_admin)
        on delete cascade
        on update cascade

)engine = InnoDB;
create table if not exists pelicula(

	id_pelicula int not null auto_increment,
    id_horario date not null,
    nombre varchar(60),
    lenguaje varchar(60),
    sinopsis varchar(200),
    costo float,
    
    primary key(id_pelicula),
    
    constraint fk_pelicula foreign key (id_horario)
		references horario(id_horario)
        on delete cascade
        on update cascade

)engine = InnoDB;
create table if not exists detalles_pelicula(

	no_sala int,
    id_pelicula int,
    
    primary key(no_sala, id_pelicula),
    
    constraint fk_detalles_asiento foreign key (no_sala)
		references sala(no_sala)
        on delete cascade
        on update cascade,
        
	constraint fk_detalles_pelicula foreign key (id_pelicula)
		references pelicula(id_pelicula)
        on delete cascade
        on update cascade

)engine = InnoDB;