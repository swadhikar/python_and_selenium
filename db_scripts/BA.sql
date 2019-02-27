--drop table employee;

CREATE TABLE EMPLOYEE(
  EMP_ID    NUMBER(5)    NOT NULL PRIMARY KEY,
  DEPT_ID   NUMBER(5)    NOT NULL,
  FIRSTNAME VARCHAR2(20) NOT NULL, 
  LASTNAME  VARCHAR2(20) NOT NULL, 
  JOB       VARCHAR2(20),
  HIREDATE  DATE,         
  SALARY    NUMBER(10,2),
  FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(DEPARTMENT_ID)
);

CREATE TABLE DEPARTMENT(
  DEPARTMENT_ID     NUMBER(5) NOT NULL PRIMARY KEY,
  DEPARTMENT_NAME   VARCHAR2(20) NOT NULL
);

select count(*) from employee;

describe employee;

insert into DEPARTMENT values (1, 'Sales');
insert into DEPARTMENT values (2, 'Software');

insert into employee values (2000, 1, 'Swadhikar', 'C', 'SrEngineer', TO_DATE('2014/04/09 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 4300);

insert into employee values (2001, 2, 'Scott', 'Beaulieau', 'Manager', TO_DATE('2010/03/10 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 8400);

insert into employee values (2002, 1, 'Morris', 'Shawn', 'SrManager', TO_DATE('2009/01/17 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 10000);

insert into employee values (2003, 1, 'Tim', 'Knitter', 'SrEngineer', TO_DATE('2011/03/30 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 6000);

insert into employee values (2004, 1, 'Sidney', 'Sheldon', 'Engineer', TO_DATE('2013/10/10 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 3500);

insert into employee values (2005, 1, 'Michael', 'Slater', 'JrEngineer', TO_DATE('2014/11/13 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 3000);

insert into employee values (2006, 2, 'David', 'Seller', 'SrEngineer', TO_DATE('2010/04/09 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 5400);

insert into employee values (2007, 2, 'Mark', 'Henry', 'EngineerII', TO_DATE('2011/01/15 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 6000);

insert into employee values (2008, 1, 'Nicolas', 'Jaden', 'EngineerI', TO_DATE('2013/7/16 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 6500);

insert into employee values (2009, 1, 'Paul', 'Faulkner', 'EngineerII', TO_DATE('2012/03/10 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 6500);

insert into employee values (2010, 2, 'Balaji', 'S', 'Manager', TO_DATE('2009/03/01 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 1000);

--Return employee record with highest salary
select * from employee where salary = (select MAX(salary) from employee);

--Return highest salary in employee table
select MAX(salary) from employee;

--Return second highest salary in employee table
select MAX(salary) from employee where salary not in (select MAX(salary) from employee);

select * from employee;
select * from department;

--Return range of employee based on values
--  a. employee id
select * from employee where emp_id between 2001 and 2007;

--  b. hiredate
select * from employee where hiredate between TO_DATE('01/04/10', 'DD/MM/YY') 
and TO_DATE('01/04/14', 'DD/MM/YY');

--  c. salary
select * from employee where salary between 3000 and 5000;

--Return employee name highest salary and department
select e.EMP_ID, e.FIRSTNAME, e.LASTNAME, e.SALARY, d.DEPARTMENT_NAME
from EMPLOYEE e INNER JOIN DEPARTMENT d ON (e.DEPT_ID = d.DEPARTMENT_ID)
where e.SALARY = (select MAX(salary) from EMPLOYEE);


--Return highest salary for each department
select e.EMP_ID, e.FIRSTNAME, e.LASTNAME, e.SALARY, d.DEPARTMENT_NAME
from EMPLOYEE e INNER JOIN DEPARTMENT d ON (e.DEPT_ID = d.DEPARTMENT_ID)
where e.SALARY IN (select MAX(salary) from employee group by department_id);


/*
  SQL Interview practise questions
*/

CREATE TABLE emp(emp_id varchar(5) NOT NULL,  
emp_name varchar(20) NULL,  
dt_of_join date NULL,  
emp_supv varchar(5) NULL,  
CONSTRAINT emp_id PRIMARY KEY(emp_id) ,  
CONSTRAINT emp_supv FOREIGN KEY(emp_supv) REFERENCES emp(emp_id));  

describe emp;

--Insert data
Insert into emp values (2001, 'Varun Sarkar', TO_DATE('2009/03/01 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), null);

Insert into emp values (2002, 'Akshay Patel', TO_DATE('2009/03/01 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 2001);

Insert into emp values (2003, 'Naresh Chowdhary', TO_DATE('2009/03/01 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 2001);

Insert into emp values (2004, 'Anurag Sharma', TO_DATE('2009/03/01 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 2001);

Insert into emp values (2005, 'Das Gupta', TO_DATE('2009/03/01 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 2003);

Insert into emp values (2006, 'Ram Singh', TO_DATE('2009/03/01 10:00:44', 'yyyy/mm/dd hh24:mi:ss'), 2003);

select * from emp;

--List all employees with their supervisor names
select a.emp_id as "EMP_ID", a.EMP_NAME as "NAME", 
b.EMP_ID as "MANAGER_ID", b.EMP_NAME as "MANAGER_NAME"
from emp a, emp b
where a.emp_supv = b.emp_id;

/*SELECT a.emp_id AS "Emp_ID",a.emp_name AS "Employee Name",  
b.emp_id AS "Supervisor ID",b.emp_name AS "Supervisor Name"  
FROM employee a, employee b  
WHERE a.emp_supv = b.emp_id;  */

drop table emp;
commit;


--Join with group by and order by
create table agents(
                    agent_id    varchar2(5) NOT NULL,
                    agent_name  varchar2(20) NOT NULL,
                    CONSTRAINT agent_id PRIMARY KEY(agent_id)
);

create table orders(
                    order_id    varchar2(5) NOT NULL,
                    order_amt   number(10) NOT NULL,
                    order_adv   number(10) NOT NULL,
                    agent_code  varchar2(5) NOT NULL, 
                    CONSTRAINT order_id PRIMARY KEY(order_id),
                    CONSTRAINT agent_code FOREIGN KEY (agent_code) REFERENCES agents(agent_id)
);

insert into agents values ('A', 'Akshay');
insert into agents values ('B', 'Balaji');
insert into agents values ('C', 'Chellappa');

insert into orders values ('1', 1000, 100, 'A');
insert into orders values ('2', 2000, 200, 'B');
insert into orders values ('3', 3000, 300, 'A');
insert into orders values ('4', 4000, 400, 'C');
insert into orders values ('5', 5000, 500, 'C');
insert into orders values ('6', 5000, 500, 'B');
insert into orders values ('7', 6000, 600, 'A');

select * from agents;
select * from orders;

describe orders;

--Display agent_id, agent_name and order_amt
select a.agent_id, a.agent_name, sum(o.order_amt), sum(o.order_adv), avg(o.order_amt)
from agents a, orders o
where a.Agent_Id = o.Agent_Code
GROUP BY a.agent_id, a.agent_name
ORDER BY a.agent_id;

SELECT agents.agent_id,agents.agent_name,  
SUM(orders.order_amt)  
FROM agents, orders  
WHERE agents.agent_id=orders.agent_code  
GROUP BY agents.agent_id, agents.agent_name  
ORDER BY agents.agent_id;  


--Joining tables with primary key and foreign key
create table foods ( 
                    item_id       number(5)       Not Null,
                    item_name     varchar2(20)    Not Null,
                    company_id    number(5)       Not Null,
                    Constraint item_id Primary Key(item_id),
                    Constraint fk_company_id Foreign Key (company_id) References company(company_id)
);

create table company(
                    company_id    number(5)       Not Null,
                    company_name  varchar2(20),
                    company_city  varchar2(20),
                    Constraint company_id Primary Key(company_id)
);

insert into company values(100, '100$ Company', 'London');
insert into company values(200, '200$ Company', 'Chennai');

insert into foods values (1, 'Biscuit', 100);
insert into foods values (3, 'Chocolate', 200);
insert into foods values (2, 'Candy', 100);
insert into foods values (4, 'Icecream', 200);
insert into foods values (5, 'Juice', 200);

select * from foods;
select * from company;


--Display 'item_name', 'item_unit' from 'foods' table and 
--'company_name', 'company_city' from 'company' table where 
--city name is london
select foods.item_id, foods.item_name, company.company_city, company.company_name
from foods, company
where Foods.Company_Id = Company.Company_Id
and Company.Company_City = 'Chennai';

select foods.item_id, foods.item_name, company.company_city, company.company_name
from foods
Inner Join company ON Foods.Company_Id = Company.Company_Id
where Company.Company_City = 'Chennai';


/*
  Procedures and functions
  http://www.guru99.com/subprograms-procedures-functions-pl-sql.html
*/
--create or replace procedure welcome_msg(p_name IN varchar2)
--IS
--BEGIN
--  dbms_output.put_line('Welcome ' || p_name || '!');
--END;
--
--EXEC Welcome_Msg('Gurushankar');
--
--create or replace function 
--      welcome_msg_func(pname IN VARCHAR2)
--return varchar2
--is
--begin
--  return ('Welcome ' || pname || '!');
--end;

select welcome_msg_func('Gurushankar K') as welcome_msg from dual;


--Oracle Built-Ins
/*
  INSTR(text, string, start, occurance)	
    Gives the position of particular text in the given string.
  
    text – Main string
    string – text that need to be searched
    start – starting position of the search (optional)
    accordance – occurrence of the searched string (optional)
*/
select INSTR('AEROPLANE', 'E', 2, 2) from DUAL;

/*
  SUBSTR ( text, start, length)
    Gives the substring value of the main string.
    
    text – main string
    start – starting position
    length – length to be sub stringed
*/

select SUBSTR('AEROPLANE', 1, 5) from DUAL; -- AEROP
select SUBSTR('AEROPLANE', 5, 9) from DUAL; -- PLANE

/*
  UPPER ( text )	Returns the uppercase of the provided text
*/
select UPPER('aeropLane') from dual;

/*
  LOWER ( text )	Returns the lowercase of the provided text
*/
select LOWER('Aeroplane') from dual;

/*
  INITCAP ( text)	Returns the given text with the starting letter in upper case.
*/
select INITCAP('AEROPLANE') from dual; --> Aeroplane

/*
  LENGTH ( text )	Returns the length of the given string	
*/
select LENGTH('aeroplane') from dual;

--Function to return the length of the string input
--create or replace function size_of(p_name varchar2)
--return number
--is
--begin
--  return LENGTH(p_name);
--end;

select size_of('help me in this text size') from dual;
select size_of('') from dual;

/*
  SYSDATE	Returns the current date and time of the server
*/
select SYSDATE from dual;

/*
  ADD_MONTHS (date, no.of months)	Adds the given months to the date
*/
select ADD_MONTHS(to_date('2015-01-01', 'YYYY-MM-DD'), 5) as AFTER_5_MONTHS from dual;
select ADD_MONTHS(SYSDATE, 5) as FIVE_MONS_FROM_NOW from dual;


select SYSDATE, TRUNC(SYSDATE) from DUAL;
select SYSDATE, ROUND(SYSDATE) from DUAL;
select MONTHS_BETWEEN(SYSDATE+62, SYSDATE) from DUAL;

--Is this printed there
describe emp;
select * from emp;
insert into emp values(2007, 'Ramesh Verma', TO_DATE('2014/04/09', 'yyyy/mm/dd'), 2003);