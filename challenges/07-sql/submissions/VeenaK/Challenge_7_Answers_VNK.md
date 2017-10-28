
## Challenge 7

### Veena Kumar

#### 7.1
**What customers are from the UK?**

```sql
SELECT * FROM [Customers] WHERE Country = 'UK';
```

| CustomerName          | ContactName       | Address                      | City   |
|-----------------------|-------------------|------------------------------|--------|
| Around the Horn       | Thomas Hardy      | 120 Hanover Sq.              | London |
| B's Beverages         | Victoria Ashworth | Fauntleroy Circus            | London |
| Consolidated Holdings | Elizabeth Brown   | Berkeley Gardens 12 Brewery  | London |
| Eastern Connection    | Ann Devon         | 35 King George               | London |
| Island Trading        | Helen Bennett     | Garden House Crowther Way    | Cowes  |
| North/South           | Simon Crowther    | South House 300 Queensbridge | London |
| Seven Seas Imports    | Hari Kumar        | 90 Wadhurst Rd.              | London |


#### 7.2
**What is the name of the customer who has the most orders?**

```sql
SELECT Customers.CustomerName, COUNT(*) AS Count
FROM Customers
JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
GROUP BY Customers.CustomerName
ORDER BY Count
DESC LIMIT 1;
```

Ernst Hendel; Quantity: 10

#### 7.3
**What supplier has the highest average product price?**

```sql
SELECT AVG(Price) AS PriceAvg, SupplierID
FROM [Products]
GROUP BY SupplierID
ORDER BY PriceAvg DESC;
```

Supplier #18 = Aux joyeux ecclésiastiques

#### 7.4
**How many different countries are their customers from? (Hint: Consider DISTINCT.)**

```sql
SELECT COUNT(DISTINCT Country) FROM Customers;

```
21 different countries

#### 7.5
**What category appears in the most orders?**

```sql
SELECT Categories.CategoryName
FROM Categories, Products, OrderDetails
WHERE Products.CategoryID = Categories.CategoryID
AND OrderDetails.ProductID = Products.ProductID
GROUP BY Products.ProductID
ORDER BY SUM(OrderDetails.Quantity)DESC
LIMIT 1;
```
Dairy Products appears in most orders.


#### 7.6
**What was the total cost for each order?**

```sql
SELECT OrderID, SUM(Quantity*Price) as Total
FROM OrderDetails 
JOIN Products ON OrderDetails.ProductID = Products.ProductID 
GROUP BY OrderID;
```

OrderID	SUM(Quantity*Price)
10248	566
10249	2329.25
10250	2267.25
10251	839.5
10252	4662.5
10253	1806
10254	781.5
10255	3115.75
10256	648
10257	1400.5
....


#### 7.7
**What employee made the most sales (by total cost)?**

```sql
SELECT Employees.FirstName, Employees.LastName, SUM(OrderDetails.Quantity*Products.Price) as TotalSales
FROM OrderDetails, Employees, Products, Orders
WHERE Products.ProductID = OrderDetails.ProductID
AND Orders.OrderID = OrderDetails.OrderID
AND Orders.EmployeeID = Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY TotalSales DESC
LIMIT 1;
```

FirstName	LastName	TotalSales
Margaret	Peacock	105696.49999999999


#### 7.8
**What employees have BS degrees? (Hint: Look at the LIKE operator.)**

```sql
SELECT FirstName,LastName
FROM Employees
WHERE Notes LIKE "%BS%";
```

FirstName	LastName
Janet	Leverling
Steven	Buchanan


#### 7.9
**What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)**

```sql
SELECT Suppliers.SupplierName, COUNT(Products.SupplierID) AS Counts, AVG(Price)
FROM Suppliers, Products
WHERE Suppliers.SupplierID = Products.SupplierID
GROUP BY Products.SupplierID
HAVING Counts > 2
ORDER BY AVG(Price) DESC
LIMIT 1;
```

SupplierName	Counts	AVG(Price)
Tokyo Traders	3	46





