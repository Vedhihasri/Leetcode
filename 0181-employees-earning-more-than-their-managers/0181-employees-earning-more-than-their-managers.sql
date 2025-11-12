# Write your MySQL query statement below
select b.name as Employee
from Employee a
join Employee b 
on a.id=b.managerId
where a.salary<b.salary 