
#### 7.1 What customers are from the UK?
**7 of them, I won't list**
```sql
SELECT***
FROM Customers 
WHERE Country = 'UK'
```


### 7.2 What is the name of the customer who has the most orders?
**Ernst Handel  count = 10**

```sql
SELECT c.CustomerName, COUNT(*)
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY o.CustomerID
ORDER BY 2 DESC
LIMIT 1
```


### 7.3 What supplier has the highest average product price?
** Aux joyeux ecclésiastiques avg = 140.75**

```sql
SELECT s.SupplierName, AVG(p.Price) 'Average Product Price'
FROM Products p 
INNER JOIN Suppliers s
ON s.SupplierID = p.SupplierID
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1
```



### 7.4 How many different countries are their customers from?
**21**

```sql
SELECT COUNT(DISTINCT Country) 'Country Count'
FROM Customers
```



### 7.5 What category appears in the most orders?
**Dairy products count = 100**

```sql
SELECT c.CategoryName, COUNT(*) 'Order Appearances'
FROM OrderDetails od
INNER JOIN Products p 
ON od.ProductID = p.ProductID
INNER JOIN Categories c
ON p.CategoryID = c.CategoryID
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1
```



### 7.6 What was the total cost for each order?
**bonus for customer name**

```sql
SELECT c.CustomerName, od.OrderID, SUM(p.Price*od.Quantity) AS Cost
FROM OrderDetails od
INNER JOIN Products p 
ON od.ProductID = p.ProductID
INNER JOIN Orders o
ON od.OrderID = o.OrderID
INNER JOIN Customers c
ON o.CustomerID = c.CustomerID
GROUP BY 2
ORDER BY 3 DESC
```



### 7.7 What employee made the most sales (by total cost)? 
**Margaret Peacock with $105696.49**

```sql
SELECT e.FirstName, e.LastName, e.EmployeeID,
 SUM(p.Price*od.Quantity) AS Sales
FROM OrderDetails od
INNER JOIN Products p 
ON od.ProductID = p.ProductID
INNER JOIN Orders o
ON od.OrderID = o.OrderID
INNER JOIN Employees e
ON o.EmployeeID = e.EmployeeID
GROUP BY e.EmployeeID
ORDER BY 4 DESC
LIMIT 1
```



### 7.8 What employees have BS degrees?
**Steve and Janet  Steve's is a BSC which is equivalent AND Notes NOT LIKE '%BSC%' would remove it if you just wanted BS**
```sql
SELECT**
FROM Employees
WHERE Notes LIKE '%BS%'
```



### 7.9 What supplier of three or more products has the highest average product price?
**Tokyo Traders  3 products with an average of $46 each**
```sql
SELECT s.SupplierName, AVG(p.Price) 'Average Price given 3 or more products',
COUNT(p.SupplierID) 'Number of Products'
FROM Products p
INNER JOIN Suppliers s
ON p.SupplierID = s.SupplierID
GROUP BY p.SupplierID
HAVING COUNT(p.SupplierID) >=3
ORDER BY 2 DESC
LIMIT 1
```
