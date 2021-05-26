create table if not exists Employee (
	id serial primary key,
	name varchar(40) not null unique,
	dept_id integer references dept(id),
	supervisor_id integer references Supervisor(id)
);

create table if not exists Dept (
	id serial primary key,
	name varchar(40) not null unique
);

create table if not exists Supervisor (
	id serial primary key,
	name varchar(40) not null unique,
	employee_id integer references Employee(id),
	dept_id integer references Dept(id)
);
