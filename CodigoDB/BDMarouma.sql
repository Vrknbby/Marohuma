use master
-------------------------------------
create database ProyectoMarohuma
use ProyectoMarohuma
--Cuando necesite borrarla o directamente eliminandola en la barra lateral
drop database ProyectoMarohuma

create table Especialidad(
	IdEspecialidad int primary key not null,
	Descripcion varchar(30) not null
);


create table Rol(
	IdRol int primary key not null,
	Descripcion varchar(30) not null
);


create table Empleado(
	DniEmpleado varchar(8) primary key not null,
	IdEspecialidad int not null,
	IdRol int not null,
	Nombre varchar(20) not null,
	Apellido varchar(20) not null,
	FechaNacimiento date not null,
	Sueldo float not null,
	eMail varchar(50) not null,
	foreign key (IdEspecialidad) references Especialidad(IdEspecialidad),
	foreign key (IdRol) references Rol(IdRol) 
);
ALTER TABLE Empleado
DROP COLUMN Edad;

ALTER TABLE Empleado
ADD Estado varchar(20) DEFAULT 'Activo' NOT NULL;

select * from viewEmpleados

create table Usuario(
	IdUsuario int IDENTITY(1,1) primary key not null,
	DniEmpleado varchar(8) not null,
	NombreUsuario varchar(20) not null,
	Contraseña varchar(15) not null,
	foreign key (DniEmpleado) references Empleado(DniEmpleado)
);

create table Servicio(
	IdServicio varchar(30) primary key not null,
	NumeroDocumento varchar(11) not null,
	IdUsuario int not null,
	NombreProyecto varchar(100) not null,
	TipoServicio varchar(30) not null,
	InicioProyecto date not null,
	FinProyecto date not null,
	CantEmpleados int not null,
	DireccionProyecto varchar(100) not null,
	Costo float not null,
	foreign key (NumeroDocumento) references Cliente(NumeroDocumento),
	foreign key (IdUsuario) references Usuario(IdUsuario)
);

ALTER TABLE Servicio
ADD Estado varchar(30) NOT NULL DEFAULT 'En Proceso';


select * from Documento where IdServicio = 'Centro Penitenciario E-100'

insert into Especialidad(IdEspecialidad,Descripcion) values (1,'UsuarioSistema');
insert into Especialidad(IdEspecialidad,Descripcion) values (2,'Obrero');

insert into Rol(IdRol,Descripcion) values (1,'Administrador');
insert into Rol(IdRol,Descripcion) values (2,'Inventario');
insert into Rol(IdRol,Descripcion) values (3,'Colaborador');

insert into Empleado(DniEmpleado,IdEspecialidad,IdRol,Nombre,Apellido,Edad,FechaNacimiento,Sueldo,eMail) values ('60914233',1,1,'Nicolas','Barrantes',20,'2003-10-27',2000.0,'barrantesnicolas27@gmail.com');
insert into Empleado(DniEmpleado,IdEspecialidad,IdRol,Nombre,Apellido,Edad,FechaNacimiento,Sueldo,eMail) values ('60771457',1,2,'Rodrigo','Tocto',18,'2005-05-10',2000.0,'rodrigotocto.55@gmail.com');

insert into Usuario(DniEmpleado,NombreUsuario,Contraseña) values ('60914233','BN60914233','60914233');
insert into Usuario(DniEmpleado,NombreUsuario,Contraseña) values ('60771457','TR60771457','60771457');

select * from Especialidad;
select * from Empleado;
select * from Empleado where DniEmpleado='60914233';

select * from Usuario where NombreUsuario='NB60914233';


CREATE VIEW viewEmpleados AS
    SELECT em.DniEmpleado, es.Descripcion as Especialidad, ro.Descripcion as Rol, em.Nombre, em.Apellido, em.FechaNacimiento, em.Sueldo, em.eMail, em.Estado
    FROM Empleado em
    INNER JOIN Especialidad es ON em.IdEspecialidad=es.IdEspecialidad 
    INNER JOIN Rol ro ON em.IdRol=ro.IdRol;


select * from viewEmpleados;
select * from Empleado
select * from Rol
select * from Usuario

create table Cliente(
	NumeroDocumento varchar(11) primary key not null,
	Nombre varchar(100) not null,
	TipoDocumento varchar(10) not null,
	Direccion varchar(100) not null,
	Telefono varchar(9) not null
);

select * from Cliente
insert into Cliente(NumeroDocumento,Nombre,TipoDocumento,Direccion,Telefono) values ('10603645941','Patrick Rivera','RUC','Mz. G lt. 10 Coop.America','987654321')
insert into Cliente(NumeroDocumento,Nombre,TipoDocumento,Direccion,Telefono) values ('10778264656','Andre Lujan','RUC','Mz. H lt.20 Av. Los Lirios','912345678')

select NumeroDocumento from Cliente

create table Documento(
    ID varchar(50) primary key not null,
    IdServicio varchar(30) not null,
    Tipo varchar(20) not null,
    Descripcion varchar(50) not null,
    Fecha date null,
    foreign key (IdServicio) references Servicio(IdServicio)
);
drop table Documento

select * from Documento
select * from Servicio
create table Proveedor(
	Ruc varchar(11) primary key not null,
	Nombre varchar(50) unique not null,
	RazSocial varchar(200) not null,
	Direccion varchar (100) not null,
	Telefono varchar(9) not null
);

create table Pedido(
	NumPedido varchar(11) primary key not null,
	RucPro varchar(11) not null,
	TipoDoc varchar(20) not null,
	Fecha date not null,
	DetalleRegistrado BIT NOT NULL
	foreign key (RucPro) references Proveedor(Ruc)
);

ALTER TABLE Pedido
ADD DetalleRegistrado BIT NOT NULL DEFAULT 0;

select * from Pedido

create table Material(
	IdMaterial int IDENTITY(1,1) primary key not null,
	IdServicio varchar(30) not null,
	Nombre varchar(30)not null,
	Descripcion varchar(200) not null,
	Stock int not null,
	UnidadMedida varchar(20) not null,
	Frente varchar(50) not null,
);



create table DetalleCompra(
	IdDetalle int IDENTITY(1,1) primary key not null,
	IdServicio varchar(30) not null,
	NumPedido varchar(11) unique not null,
	IdMaterial int not null,
	Cantidad int not null,
	PrecioU float not null,
	PrecioP float not null,
	MetodoPago varchar(30) not null,
	Estado varchar(20) not null,
	foreign key (IdServicio) references Servicio(IdServicio),
	foreign key (NumPedido) references Pedido(NumPedido),
	foreign key (IdMaterial) references Material(IdMaterial)
);

create table MovimientoMaterial(
    IdMovimiento int IDENTITY(1,1) primary key not null, 
    IdUsuario int not null,
    IdMaterial int not null,
    DniEmpleado varchar(8)not null,
    IdServicio varchar(30) not null,
    TipoMovimiento varchar(20) not null,
    Frente varchar(50) not null,
    cantidad int not null,
    Fecha date not null,
    foreign key (IdUsuario) references Usuario(IdUsuario),
    foreign key (IdMaterial) references Material(IdMaterial)
);

ALTER TABLE MovimientoMaterial
ADD Fecha date not null;

CREATE VIEW VistaDetalleCompra AS
SELECT 
    DC.IdDetalle, DC.IdServicio,DC.NumPedido, M.Nombre AS NombreMaterial, DC.Cantidad, DC.PrecioU, DC.PrecioP,DC.MetodoPago,DC.Estado
FROM 
    DetalleCompra DC
JOIN 
    Material M ON DC.IdMaterial = M.IdMaterial;
select * from DetalleCompra

CREATE VIEW VistaPedido AS
SELECT P.NumPedido, PR.Nombre AS NombreProveedor, P.TipoDoc, P.Fecha, P.DetalleRegistrado
FROM Pedido P
JOIN Proveedor PR ON P.RucPro = PR.Ruc;

drop table DetalleCompra
drop table MovimientoMaterial
drop table Material
drop table Pedido

select * from MovimientoMaterial
select * from Material

CREATE VIEW VistaMovimientoMaterial AS
SELECT 
    MM.IdMovimiento,
    U.NombreUsuario AS NombreUsuario,
    M.Nombre AS NombreMaterial,
    MM.DniEmpleado,
    MM.IdServicio,
    MM.TipoMovimiento,
    MM.Frente,
    MM.Cantidad
FROM 
    MovimientoMaterial MM
JOIN
    Usuario U ON MM.IdUsuario = U.IdUsuario
JOIN
    Material M ON MM.IdMaterial = M.IdMaterial;

select IdServicio,Nombre from Material
select IdServicio,Nombre from Material WHERE IdServicio = 'PenHouse P-200'
SELECT Estado FROM DetalleCompra WHERE IdDetalle = 1
select * from VistaMovimientoMaterial

delete from Servicio