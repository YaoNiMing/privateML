# Kaushik Challenge 7 Submission  
### SQL Challenges
**Challenge 0 - Practice Example**

What customers are from Sweden?

```sql
SELECT * FROM Customers WHERE Country='Sweden';
```

>Berglunds snabbköp  	Christina Berglund  
Folk och fä HB  	Maria Larsson   

---

**Challenge 1**

What customers are from the UK?

```sql
SELECT * FROM Customers WHERE Country='UK';
```

>4	Around the Horn	Thomas Hardy	120 Hanover Sq.	London	WA1 1DP	UK  
11	B's Beverages	Victoria Ashworth	Fauntleroy Circus	London	EC2 5NT	UK  
16	Consolidated Holdings	Elizabeth Brown	Berkeley Gardens 12 Brewery	London	WX1 6LT	UK  
19	Eastern Connection	Ann Devon	35 King George	London	WX3 6FW	UK  
38	Island Trading	Helen Bennett	Garden House Crowther Way	Cowes	PO31 7PJ	UK  
53	North/South	Simon Crowther	South House 300 Queensbridge	London	SW7 1RZ	UK  
72	Seven Seas Imports	Hari Kumar	90 Wadhurst Rd.	London	OX15 4NB	UK   

---


**Challenge 2**

What is the name of the customer who has the most orders?

```sql
SELECT Customers.CustomerName, COUNT() AS order_count 
FROM Customers, Orders
WHERE Customers.CustomerID=Orders.CustomerID
GROUP BY Customers.CustomerName ORDER BY COUNT() DESC;
```

>CustomerName	order_count  
Ernst Handel	10  
QUICK-Stop	7  
Rattlesnake Canyon Grocery	7  
Wartian Herkku	7  

---


**Challenge 3**

What supplier has the highest average product price?

```sql
SELECT Suppliers.SupplierName, AVG(Price)
FROM Suppliers, Products
WHERE Suppliers.SupplierID=Products.SupplierID 
GROUP BY Suppliers.SupplierName ORDER BY AVG(Price) DESC;
```

>SupplierName	AVG(Price)  
Aux joyeux ecclésiastiques	140.75  
Tokyo Traders	46  
Plutzer Lebensmittelgroßmärkte AG	44.678000000000004  
Gai pâturage	44.5  

---


**Challenge 4**

How many different countries are their customers from? (Hint: Consider DISTINCT.)

```sql
SELECT COUNT(DISTINCT Country) FROM Customers
```

>21  

---


**Challenge 5**

What category appears in the most orders?

```sql
SELECT combined.CategoryName, MAX(combined.count) 
FROM 
    (SELECT Categories.CategoryID, Categories.CategoryName, COUNT(DISTINCT OrderDetails.OrderID) AS count
    FROM OrderDetails 
    	INNER JOIN Products on OrderDetails.ProductID = Products.ProductID 
    	INNER JOIN Categories on Products.CategoryID = Categories.CategoryID 
   		GROUP BY Categories.CategoryID
    	ORDER BY 3 DESC) 
 	AS combined;
```

>Beverages	80  

---

**Challenge 6**

What was the total cost for each order?

```sql
SELECT OrderDetails.OrderID, (OrderDetails.Quantity * Products.Price) AS cost
FROM OrderDetails 
JOIN Products ON OrderDetails.ProductID = Products.ProductID 
GROUP BY OrderDetails.OrderID
ORDER BY cost DESC;

```

>OrderID	cost  
10353	13175  
10430	3850  
10324	3512  
10316	3451  

---


**Challenge 7**

What employee made the most sales (by total cost)?

```sql
SELECT Employees.LastName, Employees.FirstName, (OrderDetails.Quantity * Products.Price) AS cost 
FROM OrderDetails 
JOIN Products ON OrderDetails.ProductID = Products.ProductID 
JOIN Orders ON Orders.OrderID = OrderDetails.OrderID 
JOIN Employees ON Employees.EmployeeID = Orders.EmployeeID 
GROUP BY Orders.EmployeeID 
ORDER BY cost DESC;

```

>LastName	FirstName	cost  
Peacock	Margaret	2565  
Leverling	Janet	1020  
Buchanan	Steven	954  
Callahan	Laura	547.2  
Davolio	Nancy	500  

---


**Challenge 8**

What employees have BS degrees? (Hint: Look at the LIKE operator.)

```sql
SELECT LastName, FirstName FROM Employees WHERE Notes LIKE '%BS%';

```

>LastName	FirstName  
Leverling	Janet  
Buchanan	Steven  

---


**Challenge 9**

What supplier of three or more products has the highest average product price? (Hint: Look at the HAVING operator.)

```sql
SELECT Suppliers.SupplierName, COUNT(Products.ProductID), AVG(Products.Price) 
FROM Suppliers 
JOIN Products ON Suppliers.SupplierID = Products.SupplierID 
GROUP BY Suppliers.SupplierName 
HAVING COUNT(Products.ProductID) >= 3 
ORDER BY AVG(Products.Price) DESC;

```

>SupplierName	COUNT(Products.ProductID)	AVG(Products.Price)  
Tokyo Traders	3	46  
Plutzer Lebensmittelgroßmärkte AG	5	44.678000000000004  
Pavlova, Ltd.	5	35.57  
Grandma Kelly's Homestead	3	31.666666666666668  
G'day, Mate	3	30.933333333333334  

---

