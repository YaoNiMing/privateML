# 7.1
What customers are from the UK?
```sql
SELECT * FROM Customers WHERE Country = "UK";
```
Answer:
Around the Horn
Bs Beverages
Consolidated Holdings
Eastern Connection
Island Trading
North/South
Seven Seas Imports


# 7.2
What is the name of the customer who has the most orders?
```sql
SELECT Customers.CustomerName
FROM Customers, Orders
WHERE Customers.CustomerID=Orders.CustomerID
GROUP BY CustomerName
ORDER BY COUNT(*) DESC
LIMIT 1;
```
Answer:
Ernst Handel


# 7.3
What supplier has the highest average product price?
```sql
SELECT Suppliers.SupplierName
FROM Suppliers, Products 
WHERE Suppliers.SupplierID=Products.SupplierID
GROUP BY Suppliers.SupplierName
ORDER BY AVG(Price) DESC
LIMIT 1;
```
Answer: Aux joyeux ecclésiastiques

# 7.4
How many different countries are their customers from? (Hint: Consider DISTINCT.)
```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```
Answer: 21

# 7.5
What category appears in the most orders?
```sql
SELECT Categories.CategoryName
FROM Categories, OrderDetails, Products
WHERE Categories.CategoryID = Products.CategoryID
AND Products.ProductID = OrderDetails.ProductID
AND Products.CategoryID = Categories.CategoryID
GROUP BY Categories.CategoryName
ORDER BY Count(*) DESC
LIMIT 1;
```
Answer: Dairy Products


# 7.6
What was the total cost for each order?
```sql
SELECT OrderDetails.OrderID, OrderDetails.Quantity*Products.Price
FROM OrderDetails, Products
WHERE OrderDetails.ProductID = Products.ProductID 
GROUP BY OrderDetails.OrderID
```

Answer:
OrderDetailID	OrderID	ProductID	Quantity
1	10248	11	12
2	10248	42	10
3	10248	72	5
4	10249	14	9
5	10249	51	40


# 7.7
What employee made the most sales (by total cost)?
```sql
SELECT Employees.FirstName, Employees.LastName
FROM OrderDetails, Orders, Employees, Products
WHERE OrderDetails.OrderID = Orders.OrderID
AND Employees.EmployeeID = Orders.EmployeeID
GROUP BY Employees.EmployeeID
ORDER BY OrderDetails.Quantity*Products.Price DESC
LIMIT 1;
```
Answer: Margaret Peacock


# 7.8
What employees have BS degrees? (Hint: Look at the LIKE operator.)
```sql
SELECT FirstName, LastName
FROM Employees
WHERE Notes LIKE "%BS%";
```
Answer:
Janet Leverling
Steven Buchanan


# 7.9
What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)
```sql
SELECT Suppliers.SupplierName
FROM Suppliers, Products
WHERE Suppliers.SupplierID = Products.SupplierID
GROUP BY Suppliers.SupplierName
HAVING Count(Products.ProductID) > 2
ORDER BY AVG(Products.Price) DESC
LIMIT 1;
```
Answer: Tokyo Traders