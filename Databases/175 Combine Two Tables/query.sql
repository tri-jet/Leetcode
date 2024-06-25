-- First Approach:

-- # Write your MySQL query statement below
-- Select firstName, lastName,
-- Case 
--     When Person.personId != Address.personId Then null 
--     Else city
-- End As city,
-- Case 
--     When Person.personId != Address.personId Then null 
--     Else state
-- End As state,
-- From Person, Address;

-- Second approach - didn't work because if joining, then only need to mention the left table as the right table part is mentioned in the join
Select Person.firstName, Person.lastName, Address.city, Address.state 
From Person, Address 
Left Join Address On Person.personId = Address.personId

-- Also if joining need to explicitly use dot notation to indicate where each column is coming from

--Working version:

--need to use a left join - return all records from left (Person) and records where right matches left
Select Person.firstName, Person.lastName, Address.city, Address.state 
From Person
Left Join Address On Person.personId = Address.personId