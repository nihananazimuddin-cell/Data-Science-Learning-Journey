---------------- DAY-05 --> 3/Aug/26

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    salary INT,
    city VARCHAR(30),
    joining_date DATE
);

INSERT INTO Employees (emp_id, name, department, salary, city, joining_date)
VALUES
(101, 'Alice', 'HR', 55000, 'Kochi', '2022-01-10'),
(102, 'Bob', 'IT', 72000, 'Chennai', '2021-08-15'),
(103, 'Carol', 'Finance', 48000, 'Kochi', '2023-03-21'),
(104, 'David', 'IT', 90000, 'Bengaluru', '2020-06-18'),
(105, 'Emma', 'HR', 65000, 'Kochi', '2019-12-05');

select * from Employees;
--====================================================================================

--1.Display all employees earning more than ₹50,000.
select name, salary from employees where salary>50000;

--2.Display employees who:work in the IT department,earn more than ₹70,000
select name, department, salary from Employees where department = 'IT' and salary > 70000;

--3.Display all employees ordered by salary from highest to lowest.
select name, salary from Employees order by salary desc;

--4.Find the highest salary.
select max(salary) as Highest_Salary from Employees;

--5.Count the total number of employees.
select count(*) as Total_Employees from Employees;

--BONUS QN.:Display all employees from Kochi, ordered by their joining date (oldest employee first).
select name, joining_date from Employees where city = 'Kochi' order by joining_date; 

