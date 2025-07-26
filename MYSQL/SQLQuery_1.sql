create schema hr;
go

create table hr.candidates(
    id INT PRIMARY KEY IDENTITY,
    fullname VARCHAR(100) not null 

)

select * from hr.candidates


create table hr.employees(
    id INT PRIMARY KEY IDENTITY,
    fullname VARCHAR(100) not NULL
)
DROP TABLE hr.employees;

insert into 
    hr.candidates(fullname) VALUES
    ('John Doe'),
    ('Lily Bush'),
    ('Peter Drucker'),
    ('Jane Doe');

insert into 
    hr.employees(fullname) VALUES
    ('John Doe'),
    ('Jane Doe'),
    ('Michael Scott'),
    ('Jack Sparrow');

select * from hr.candidates;
select * from hr.employees;


select * from hr.candidates c 
    inner join  hr.employees e 
    on e.fullname = c.fullname; 
       