------- Day 07---------------------5/Aug/2026-----------------------------------
select * from employees;

-- Display all employee names.
select name from Employees;

-- Display employees whose salary is greater than 50000.
select name, salary from Employees where salary>50000;

-- Display all employees ordered by salary in descending order.
select name, salary from employees order by salary desc;

-- Display employees whose salary is between 40000 and 60000. (Bonus)
select name, salary from Employees where salary between 40000 and 60000;