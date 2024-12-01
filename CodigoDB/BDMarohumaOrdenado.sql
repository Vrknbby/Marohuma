-- Creación de la base de datos y cambio a ella
use master
-------------------------------------
create database ProyectoMarohuma
use ProyectoMarohuma

-- Creación de tablas
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
    Estado varchar(20) DEFAULT 'Activo' NOT NULL,
    foreign key (IdEspecialidad) references Especialidad(IdEspecialidad),
    foreign key (IdRol) references Rol(IdRol) 
);

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
    Estado varchar(30) NOT NULL DEFAULT 'En Proceso',
    foreign key (NumeroDocumento) references Cliente(NumeroDocumento),
    foreign key (IdUsuario) references Usuario(IdUsuario)
);

create table Cliente(
    NumeroDocumento varchar(11) primary key not null,
    Nombre varchar(100) not null,
    TipoDocumento varchar(10) not null,
    Direccion varchar(100) not null,
    Telefono varchar(9) not null
);

create table Documento(
    ID varchar(15) primary key not null,
    IdServicio varchar(30) not null,
    Tipo varchar(20) not null,
    Descripcion varchar(50) not null,
    Fecha date null,
    foreign key (IdServicio) references Servicio(IdServicio)
);

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
    DetalleRegistrado BIT NOT NULL,
    foreign key (RucPro) references Proveedor(Ruc)
);

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

-- Creación de vistas
CREATE VIEW viewEmpleados AS
    SELECT em.DniEmpleado, es.Descripcion as Especialidad, ro.Descripcion as Rol, em.Nombre, em.Apellido, em.FechaNacimiento, em.Sueldo, em.eMail, em.Estado
    FROM Empleado em
    INNER JOIN Especialidad es ON em.IdEspecialidad=es.IdEspecialidad 
    INNER JOIN Rol ro ON em.IdRol=ro.IdRol;

CREATE VIEW VistaDetalleCompra AS
SELECT 
    DC.IdDetalle, DC.IdServicio,DC.NumPedido, M.Nombre AS NombreMaterial, DC.Cantidad, DC.PrecioU, DC.PrecioP,DC.MetodoPago,DC.Estado
FROM 
    DetalleCompra DC
JOIN 
    Material M ON DC.IdMaterial = M.IdMaterial;

CREATE VIEW VistaPedido AS
SELECT P.NumPedido, PR.Nombre AS NombreProveedor, P.TipoDoc, P.Fecha, P.DetalleRegistrado
FROM Pedido P
JOIN Proveedor PR ON P.RucPro = PR.Ruc;

CREATE VIEW VistaMovimientoMaterial AS
SELECT 
    MM.IdMovimiento,
    U.NombreUsuario AS NombreUsuario,
    M.Nombre AS NombreMaterial,
    MM.DniEmpleado,
    MM.IdServicio,
    MM.TipoMovimiento,
    MM.Frente,
    MM.Cantidad,
    MM.Fecha
FROM 
    MovimientoMaterial MM
JOIN
    Usuario U ON MM.IdUsuario = U.IdUsuario
JOIN
    Material M ON MM.IdMaterial = M.IdMaterial;

select * from Material;
select * from viewEmpleados;
select * from Especialidad;
select * from Empleado;
select * from Rol;
select * from Usuario;
select * from Servicio;
select * from Cliente;
select * from Documento;
select * from VistaDetalleCompra;
select * from VistaPedido;
select * from VistaMovimientoMaterial;
select * from MovimientoMaterial;
select * from DetalleCompra;
select * from Pedido;

-- DROP statements
drop view VistaDetalleCompra;
drop view VistaPedido;
drop view VistaMovimientoMaterial;
drop table MovimientoMaterial;
drop table DetalleCompra;
drop table Material;
drop table Pedido;
drop table Proveedor;
drop table Cliente;
drop table Documento;
drop table Servicio;
drop table Usuario;
drop table Empleado;
drop table Rol;
drop table Especialidad;