Select e2.name As Employee From Employee e1
Inner Join Employee e2 On e1.id = e2.managerId
Where e1.salary < e2.salary

-- Output requires column to be called Employee
-- Need to use inner join as matching values 
-- As analysing with relationships within a single table,
-- need to self-join - thus Employee e1 = Managers, e2 = Employees
-- Then ensure the id for managers in e2 == employee's manager id
-- Check manager's salary is less than employee's salary 