
/* 
The following includes test code of the procedures and dataviews for the new Bank Corp Ltd client database
*/

/* 
This procedure creates a new customer called Barry Thomas and adds that new customer as an associate to existing customer with CustomerId 2.
*/

EXEC CreateNewCustomerAndAssociation @NewCustomerName = "Barry Thomas", @NewCustomerTypeCodeId = 1, @ExistingCustomerId = 2, @AssociationCodeId = 7;

/* 
We confirm this has worked by viewing the Customers table and Associations table 
*/

SELECT * FROM Customers
SELECT * FROM Associations

/* 
To test the DeleteCustomer procedure we first need to view records for the customer
*/

SELECT * FROM Associations
 WHERE 1 IN (Customer1Id, Customer2Id)

SELECT * 
  FROM Securities AS S
       INNER JOIN Accounts AS A
       ON S.AccountID = A.AccountId
 WHERE A.CustomerId = 1

SELECT * FROM Accounts
 WHERE CustomerId = 1

SELECT * FROM Addresses
 WHERE CustomerId = 1

SELECT * FROM Customers
 WHERE CustomerID = 1

/*
Then we need to run the DeleteCustomer procedure and view the records again using the same code as above
*/

EXEC DeleteCustomer @CustomerId = 1;




/* 
To test the DeleteTypeCode we just need to run the procedure
*/
EXEC DeleteTypeCode @TypeCodeId = 1;


/*
We can then confirm the procedure was successful by check the deleted types view 
*/

SELECT * FROM vwDeletedTypes;


/*
To test the Customer Associations view we generate a select from the table
This should show all the currently existing associations in both directions
*/

SELECT * FROM vwCustomerAssociations

