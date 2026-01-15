select max(salary) as SecondHighestSalary   
from Employee
where employee.salary < (select max(salary) from Employee)