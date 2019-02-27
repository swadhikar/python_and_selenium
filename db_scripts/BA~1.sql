CREATE TABLE employee (
         empno      NUMBER(5) PRIMARY KEY,
         firstname  VARCHAR2(15) NOT NULL,
         lastname   VARCHAR2(15) NOT NULL,
         job        VARCHAR2(10),
         hiredate   DATE DEFAULT (sysdate),
         photo      BLOB,
         sal        NUMBER(10,2)
);

--drop table employee;

insert into employee values(1, 'Anil', 'Chowdhary', 'Manager', null, null, 100000);
insert into employee values(2, 'Ramesh', 'Powar', 'Manager', null, null, 400000);
insert into employee values(3, 'Sunil', 'Narine', 'Manager', null, null, 500000);
insert into employee values(4, 'Rajesh', 'Sinha', 'Manager', null, null, 600000);
insert into employee values(5, 'Kiran', 'Bedi', 'Manager', null, null, 700000);
insert into employee values(6, 'Anurag', 'Sharma', 'Manager', null, null, 800000);
insert into employee values(7, 'Hari', 'Shravan', 'Manager', null, null, 900000);
insert into employee values(8, 'Mohan', 'Kumar', 'Manager', null, null, 100000);
insert into employee values(9, 'Anand', 'Kannan', 'Manager', null, null, 500000);
insert into employee values(10, 'Maria', 'Thomas', 'Manager', null, null, 400000);
insert into employee values(11, 'Vinitha', 'Mahadevan', 'Engineer-II', null, null, 300000);

insert into employee values(12, 'Rajan', 'Mahadevan', 'Engineer-I', null, null, 300000);
insert into employee values(13, 'Vinod', 'Mahadevan', 'Programmer', null, null, 300000);
insert into employee values(14, 'Vivek', 'Mahadevan', 'Programmer-II', null, null, 300000);

insert into employee values(15, 'Aneesh', 'Raj', 'Engineer-I', null, null, 300000);
insert into employee values(16, 'Raman', 'Manoj', 'Programmer', null, null, 300000);
insert into employee values(17, 'Arul', 'Gowda', 'Programmer-II', null, null, 300000);

insert into employee values(20, 'Rajan', 'Mahadevan', 'Engineer-I', null, null, 300000);
insert into employee values(21, 'Vinod', 'Mahadevan', 'Programmer', null, null, 300000);


select count( * ) from employee;

select firstname, lastname from employee;
select DISTINCT firstname, lastname from employee;

select DISTINCT job from employee;

-- SQL case manipulation
CREATE TABLE
            example (
                      first     varchar2(30)
            );
          
select * from example;
select upper('hello world') from dual;
insert into example values('swadhi');
insert into example values(upper('swadhi'));
insert into example values(initcap('swadhi'));
insert into example values (lower('I AM SMALLER IN TABLE'));