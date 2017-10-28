SQL Challenges

Challenge 1

```sql
SELECT CustomerID, Country 
FROM Customers 
WHERE Country = 'UK';
```

Challenge 2

```sql
SELECT Customers.CustomerName, COUNT(*) AS counter 
FROM Customers 
JOIN Orders ON Customers.CustomerID = Orders.CustomerID 
GROUP BY Customers.CustomerName 
ORDER BY counter DESC LIMIT 1;
```

Challenge 3

```sql
SELECT Suppliers.SupplierName, AVG(Products.Price) AS price 
FROM Suppliers 
JOIN Products ON Suppliers.SupplierID = Products.SupplierID 
GROUP BY Suppliers.SupplierName 
ORDER BY price DESC LIMIT 1;
```

Challenge 4

```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```

Challenge 5

```sql
SELECT Categories.CategoryName, COUNT(*) AS counter 
FROM Categories 
JOIN Products ON Categories.CategoryID = Products.CategoryID 
JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID 
GROUP BY Categories.CategoryName 
ORDER BY counter DESC LIMIT 1;
```

Challenge 6

```sql
SELECT OrderDetails.OrderID, (OrderDetails.Quantity * Products.Price) 
FROM OrderDetails 
JOIN Products ON OrderDetails.ProductID = Products.ProductID 
GROUP BY OrderDetails.OrderID;
```

Challenge 7

```sql
SELECT Employees.LastName, Employees.FirstName, (OrderDetails.Quantity * Products.Price) AS cost 
FROM OrderDetails 
JOIN Products ON OrderDetails.ProductID = Products.ProductID 
JOIN Orders ON Orders.OrderID = OrderDetails.OrderID 
JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID 
GROUP BY Orders.EmployeeID 
ORDER BY cost DESC LIMIT 1;
```

Challenge 8

```sql
SELECT LastName, FirstName FROM Employees WHERE Notes LIKE '%BS%';
```

Challenge 9

```sql
SELECT Suppliers.SupplierName, COUNT(Products.ProductID), AVG(Products.Price) 
FROM Suppliers 
JOIN Products ON Suppliers.SupplierID = Products.SupplierID 
GROUP BY Suppliers.SupplierName 
HAVING COUNT(Products.ProductID) >= 3 
ORDER BY AVG(Products.Price) DESC LIMIT 1;
```
