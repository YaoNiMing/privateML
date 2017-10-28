1. SELECT \* FROM Customers WHERE Country=&#39;UK&#39;;

2. SELECT CustomerName, COUNT(CustomerName) FROM Customers ; (Wolski)

3. SELECT a.ProductID, a.SupplierID, AVG(a.Price),b.SupplierID, b.SupplierName FROM Products a JOIN Suppliers b ON a.SupplierID = b.SupplierID GROUP BY b.SupplierID ORDER BY AVG(a.Price)

Aux joyeux ecclésiastiques

4. SELECT COUNT(DISTINCT(Country)) FROM [Customers]

21

5. SELECT a.OrderID, a.ProductID, a.Quantity, b.ProductID, b.CategoryID, c.CategoryID, c.CategoryName FROM OrderDetails a JOIN Products b ON a.ProductID = b.ProductID  JOIN Categories c ON b.CategoryID=c.CategoryID ORDER BY a.Quantity DESC

Category 6: Meta/Poultry

6. SELECT a.OrderID, a.ProductID, a.Quantity, b.ProductID, b.Price, b.Price\*a.Quantity as Total FROM OrderDetails a JOIN Products b ON a.ProductID = b.ProductID GROUP BY a.OrderID ORDER BY Total DESC

7. SELECT k.OrderID, k.EmployeeID, l.EmployeeID, l.LastName, l.FirstName, a.OrderID, a.ProductID, a.Quantity, b.ProductID, b.Price, b.Price\*a.Quantity as Total FROM OrderDetails a JOIN Products b ON a.ProductID = b.ProductID JOIN Orders k ON a.OrderID = k.OrderID JOIN Employees l ON k.EmployeeID = l.EmployeeID GROUP BY k.EmployeeID ORDER BY Total DESC

Ans: Employee 4 Margaret Peacock

8. SELECT \* FROM [Employees] WHERE Notes LIKE &#39;%BS%&#39;

Steven Buchanan and Janet Leverling

9. SELECT a.SupplierID, AVG(a.Price), b.SupplierID, b.SupplierName FROM Products a JOIN Suppliers b ON a.SupplierID = b.SupplierID GROUP BY a.SupplierID HAVING COUNT(a.SupplierID)&gt;2 ORDER BY AVG(a.Price) DESC

Ans: Supplier Tokyo Traders, Avg Price is $46
