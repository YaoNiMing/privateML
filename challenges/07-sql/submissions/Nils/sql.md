# Challenge 7: SQL  
## 7.0
  
SELECT * FROM Customers WHERE Country='Sweden'

## 7.1  
  
SELECT * FROM Customers WHERE Country='UK'
  
## 7.2
  
SELECT CustomerName, COUNT(Orders.CustomerID)
FROM Customers JOIN Orders ON Orders.CustomerID == Customers.CustomerID
GROUP BY CustomerName
Order By Count(Orders.CustomerID) DESC

Answer: Ernst Handel

## 7.3  
  
SELECT Suppliers.SupplierName, Products.SupplierID, AVG(Products.Price) 
FROM Suppliers JOIN Products ON Products.SupplierID == Suppliers.SupplierID 
GROUP BY Products.SupplierID ORDER BY AVG(Price) DESC
  
Answer: Aux joyeux ecclésiastiques, AVG Price: 140.75  
  
## 7.4  
  
SELECT COUNT (DISTINCT Country) FROM Customers  
  
Answer: 21  
  
## 7.5  
  
SELECT CategoryName, count
FROM
   (SELECT OrderDetails.ProductID, Products.CategoryID AS id, COUNT(Products.CategoryID) AS count
      FROM OrderDetails JOIN Products ON OrderDetails.ProductID == Products.ProductID
      GROUP BY Products.CategoryID
      ORDER BY COUNT(Products.CategoryID) DESC)
JOIN Categories ON id == Categories.CategoryID
  
Answer: Dairy Products, 100 appearances  
  
## 7.6  
  
SELECT OrderID, OrderDetails.ProductID, SUM(Quantity * Price) 
  FROM OrderDetails JOIN Products ON OrderDetails.ProductID == Products.ProductID
  GROUP BY OrderID  
  
## 7.7  
  
Select LastName, FirstName, TotalSales FROM
(Select Orders.EmployeeID AS EID, oid, SUM(cost) AS TotalSales FROM
  (SELECT OrderID as oid, OrderDetails.ProductID, SUM(Quantity * Price) as cost 
    FROM OrderDetails JOIN Products ON OrderDetails.ProductID == Products.ProductID
    GROUP BY OrderID)
  JOIN Orders ON oid == Orders.OrderID
  GROUP BY EmployeeID)
JOIN Employees ON Employees.EmployeeID == EID
ORDER BY TotalSales DESC
  
Answer: Margaret Peacock: 105696.5  

## 7.8

SELECT * FROM Employees
WHERE Notes LIKE '% bs %';

Answer: Only Janet L.  

## 7.9  

SELECT Suppliers.SupplierName, Products.SupplierID, AVG(Products.Price), COUNT(ProductID) 
FROM Suppliers JOIN Products ON Products.SupplierID == Suppliers.SupplierID 
GROUP BY Products.SupplierID
HAVING COUNT(ProductID) > 2
ORDER BY AVG(Products.Price) DESC

Anwer: Tokio Traders, 46

  
