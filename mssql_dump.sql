create schema schema_test
go

create table people
(
	id int not null,
	first_name varchar(100) not null,
	last_name varchar(100) not null
)
go

create unique index people_id_uindex
	on people (id)
go

