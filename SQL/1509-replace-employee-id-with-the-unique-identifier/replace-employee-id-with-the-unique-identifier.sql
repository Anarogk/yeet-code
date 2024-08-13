# Write your MySQL query statement below
select U.unique_id, E.name
from EmployeeUNI as U
right join Employees as E
On E.id = U.id;
