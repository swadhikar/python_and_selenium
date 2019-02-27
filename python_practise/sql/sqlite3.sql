select * from EMPLOYEE;
select * from INCENTIVE;

insert into employee values (1, 'swadhikar', 'c', 10000, '08-Jun-2017', 'Computer');
insert into employee values (2, 'mohanraj', 'g', 10000, '10-Jul-2017', 'Computer');
insert into employee values (3, 'arul', 's', 15000, '20-Apr-2015', 'Mac');
insert into employee values (4, 'nandin%', 's', 15000, '20-Apr-2015', 'Mac');
insert into employee values (5, 'shravan', 'k', 25000, '22-Oct-2015', 'Mac');
insert into employee values (6, 'Anil', 'k', 25000, '22-Oct-2015', 'Windows');
insert into employee values (7, 'Rajkumar', 'k', 25000, '22-Oct-2015', 'Windows');
insert into employee values (8, 'Arun Kumar', 'k', 25000, '22-Oct-2015', 'Windows');
insert into employee values (9, 'Sriram', 'g', 10000, '10-Jul-2017', 'Mac');
insert into employee values (10, 'Rajesh', 'g', 10000, '10-Jul-2017', 'Mac');

insert into INCENTIVE values (1, '10-Jun-2018', 1000);
insert into INCENTIVE values (2, '10-Jun-2018', 1000);
insert into INCENTIVE values (3, '10-Jun-2018', 1000);

select DISTINCT DEPARTMENT from EMPLOYEE;

-- find the substring from given two indexes
select SUBSTR(FIRST_NAME, 1, 3) CODE from EMPLOYEE;

-- find the index of character in string
select INSTR(FIRST_NAME, 'r') from EMPLOYEE where FIRST_NAME = 'swadhikar';

-- right trim text
select RTRIM(FIRST_NAME) from EMPLOYEE where FIRST_NAME = 'mohanraj';

-- left trim text
select LTRIM(LAST_NAME) from EMPLOYEE where FIRST_NAME = 'arul';

-- length of string
select FIRST_NAME, length(FIRST_NAME) from EMPLOYEE e where e.EMPLOYEE_ID > 0;

-- concat (pipes)
select FIRST_NAME || '_' || LAST_NAME||'@symantec.com' EMAIL from EMPLOYEE;

-- order by firstname ascending
select * from EMPLOYEE order by FIRST_NAME asc;

-- order by lastname descending
select * from EMPLOYEE order by LAST_NAME desc;

-- order by firstname ascending, salary descending
select * from EMPLOYEE order by SALARY, FIRST_NAME

-- in function with where
select * from EMPLOYEE where FIRST_NAME not in ('arul', 'swadhikar');

-- using wild cards to search
select * from EMPLOYEE where FIRST_NAME like '%n%';
select * from EMPLOYEE where FIRST_NAME like 'a___';
select * from EMPLOYEE where FIRST_NAME like '__a%';


-- finding values in between
select * from EMPLOYEE where salary between 15000 and 24000;

-- replace text
insert into employee values (4, 'nandin%', 's', 15000, '30-Jan-2017', 'Mac');
insert into employee values (5, 'shravan', 'k', 25000, '22-Oct-2015', 'Mac');

-- group by
select DEPARTMENT, SUM(SALARY) TOTAL_SALARY from EMPLOYEE group by DEPARTMENT;
select DEPARTMENT, FIRST_NAME, MAX(SALARY) HIGHEST_SALARY from EMPLOYEE group by DEPARTMENT;
select * from EMPLOYEE;

-- Get department,no of employees in a department,total salary with respect to a
-- department from employee table order by total salary descending
select DEPARTMENT, count(FIRST_NAME), SUM(SALARY) TOTAL_SALARY from EMPLOYEE
group by DEPARTMENT order by TOTAL_SALARY desc


commit;
