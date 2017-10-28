#ch1 What customers are from Sweden?

SELECT CustomerName, ContactName FROM Customers WHERE country == 'UK'

CustomerName	ContactName
Around the Horn	Thomas Hardy
B's Beverages	Victoria Ashworth
Consolidated Holdings	Elizabeth Brown
Eastern Connection	Ann Devon
Island Trading	Helen Bennett
North/South	Simon Crowther
Seven Seas Imports	Hari Kumar

#ch2 What is the name of the customer who has the most orders?
SELECT CustomerName, sum(Quantity) AS SUM FROM Customers JOIN Orders ON Customers.CustomerID=Orders.CustomerID JOIN OrderDetails ON Orders.OrderID=OrderDetails.OrderID GROUP BY CustomerName ORDER BY SUM DESC LIMIT 1

CustomerName	SUM
Ernst Handel	1418

#ch3 What supplier has the highest average product price?
SELECT SupplierName, AVG(Price) AS Avg FROM Suppliers JOIN Products ON Suppliers.SupplierID = Products.SupplierID GROUP BY SupplierName ORDER BY Avg DESC LIMIT 1

SupplierName	Avg
Aux joyeux ecclésiastiques	140.75

#ch4 How many different countries are their customers from? (Hint: Consider DISTINCT.)
SELECT COUNT(DISTINCT(Country)) FROM [Customers]

COUNT(DISTINCT(Country))
21

#ch5 What category appears in the most orders?
SELECT CategoryID, SUM(Quantity) FROM Products JOIN OrderDetails ON Products.ProductID = OrderDetails.ProductID GROUP BY CategoryID ORDER BY SUM(Quantity) DESC LIMIT 1

CategoryID	SUM(Quantity)
4	2601

#ch6 What was the total cost for each order?
SELECT OrderID, SUM(Quantity*Price) FROM OrderDetails JOIN Products ON OrderDetails.ProductID = Products.ProductID GROUP BY OrderID

Number of Records: 196
OrderID	SUM(Quantity*Price)
10248	566
10249	2329.25
10250	2267.25
10251	839.5
... ...

#ch7 What employee made the most sales (by total cost)?
SELECT LastName, FirstName, SUM(Quantity*Price) FROM OrderDetails JOIN Products ON OrderDetails.ProductID = Products.ProductID JOIN Orders ON Orders.OrderID = OrderDetails.OrderID JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID GROUP BY Orders.EmployeeID ORDER BY SUM(Quantity*Price) DESC LIMIT 1

Number of Records: 1
LastName	FirstName	SUM(Quantity*Price)
Peacock	Margaret	105696.49999999999

#ch8 What employees have BS degrees? (Hint: Look at the LIKE operator.)
SELECT LastName, FirstName FROM [Employees] WHERE Notes LIKE '%BS%'

Number of Records: 2
LastName	FirstName
Leverling	Janet
Buchanan	Steven

#ch9 What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)
SELECT Suppliers.SupplierName, AVG(Price) FROM Suppliers JOIN Products ON Suppliers.SupplierID = Products.SupplierID GROUP BY Suppliers.SupplierID HAVING COUNT(Suppliers.SupplierID) > 3 ORDER BY AVG(Price) DESC LIMIT 1

Number of Records: 1
SupplierName	AVG(Price)
Plutzer Lebensmittelgroßmärkte AG	44.678000000000004
