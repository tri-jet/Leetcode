# Write your MySQL query statement below
Select Customers.name As Customers From Customers
Left Join Orders On Customers.id = Orders.customerId
Where Orders.CustomerId Is Null;

-- Aim: get all values of Customers that don't match in the Orders table
-- Do this by doing the Left Join to get all values of Left including
-- ones that match right table
-- then take away the intersecting values by specifying the values
-- in the right table = null, so no actual values from right table