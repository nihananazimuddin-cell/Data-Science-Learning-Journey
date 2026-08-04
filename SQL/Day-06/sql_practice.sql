-----Day 06 ------ 4/Aug/2026-------------

select * from Employees;

--Display the number of employees in each department.
select count(name) as Employee_count, department from Employees group by department;

--Display the average number of employees in each department.
select avg(Average_Emp_count), department from 
	(select count(name)as average_emp_count, department from Employees group by department)as emp_count
	group by department;

-- Display the average number of employees across all departments.
select avg(salary) as average_salary, department from Employees group by department;

--Display the highest salary in each department.
select max(salary) as max_salary, department from Employees group by department;

--Display the lowest salary in each department.
select min(salary) as min_Salary , department from Employees group by department;

--Display the total salary paid to each department.
select sum(salary) as total_salary , departmentfrom Employees group by department;