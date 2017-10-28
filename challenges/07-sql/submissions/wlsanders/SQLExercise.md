## Challenge 1: 
What customers are from the UK?

```sql
SELECT * FROM Customers WHERE Country='UK';    
```
Answer: 
CustomerName
Around the Horn
B's Beverages
Consolidated Holdings
Eastern Connection
Island Trading
North/South
Seven Seas Imports

## Challenge 2: 
What is the name of the customer who has the most orders?

```sql
SELECT
    CustomerName,
    COUNT(*) AS CustomerID
FROM
    Customers
  JOIN
    Orders
  ON
    Customers.CustomerID = Orders.CustomerID
GROUP BY CustomerName
ORDER BY CustomerID Desc;
```

Answer: Ernst Handel

## Challenge 3: 

```sql
What supplier has the highest average product price?
SELECT
    SupplierName,
    AVG(Price)
FROM
    Suppliers
  JOIN
    Products
  ON
    Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
ORDER BY Price Desc;
```

Answer: Forêts d'érables	38.9

## Challenge 4: 
How many different countries are their customers from? (Hint DISTINCT)

```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```

Answer: 21 countries. 

## Challenge 5:

What category appears in the most orders?

```sql
SELECT Categories.CategoryName, COUNT(*) AS CountOfCategories 
FROM Categories 
JOIN Products ON Categories.CategoryID = Products.CategoryID 
JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID 
GROUP BY Categories.CategoryName 
ORDER BY CountOfCategories DESC LIMIT 5;
```

Answer: Dairy Products with 100 orders. 

## Challenge 6

What was the total cost for each order?

```sql
SELECT OrderID, SUM(OrderDetails.Quantity * Products.Price) AS "Order Cost"
FROM 
OrderDetails
JOIN 
Products 
ON
OrderDetails.ProductID = Products.ProductID
GROUP BY OrderID
ORDER BY "Order Cost" Desc;
```

Answer: OrderID 10372, with a total cost of $15353.6

## Challenge 7

What employee made the most sales (by total cost)?

```sql
SELECT innerQuery.FirstName, innerQuery.LastName, innerQuery.EmployeeID, MAX(innerQuery.sales)
FROM
(select Employees.FirstName, Employees.LastName, Orders.EmployeeID, sum(Products.ProductID * Products.Price) 'sales'
FROM OrderDetails 
JOIN Orders
on OrderDetails.OrderID = Orders.OrderID
join Products 
on OrderDetails.ProductID = Products.ProductID 
join Employees 
on Employees.EmployeeID = Orders.EmployeeID
GROUP BY Orders.EmployeeID) as innerQuery
```

Answer: Margaret Peacock, EmployeeID 4 with a  total of 154490. 

## Challenge 8

What employees have BS degrees? (Hint: Look at the LIKE operator.)

```sql
SELECT FirstName, LastName
FROM 
Employees
WHERE
Notes Like '%BS%';
```
Answer: Janet Leverling and Steven Buchanan. 

## Challenge 9

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
SELECT SupplierName, AVG(Price) AS "Average Price" 
FROM 
Suppliers
JOIN
Products
ON
Suppliers.SupplierID = Products.SupplierID
GROUP BY SupplierName
```

Answer: SupplierName  Average Price
Plutzer Lebensmittelgroßmärkte AG 44.678000000000004
Pavlova, Ltd. 35.57
Specialty Biscuits, Ltd.  28.175
New Orleans Cajun Delights  20.35


