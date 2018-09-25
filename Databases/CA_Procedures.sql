
-- For testing purposes these are in place to clean up
DROP PROCEDURE CreateNewCustomerAndAssociation;
DROP PROCEDURE DeleteCustomer;
DROP PROCEDURE DeleteTypeCode;
DROP VIEW vwDeletedTypes;
DROP VIEW vwCustomerAssociations;


/* 
This first procedure CreateNewCustomerAndAssociation takes the 
details of a new customer and creates an association with an existing 
customer.
The required paramaters are:
@NewCustomerName this is a name for the new customer
@NewCustomerTypeCodeId this is the customer type using the id from the
    TypeCodes table
@ExistingCustomerId this is the id for the existing customer as from
    the customer table.
@AssociationCodeId this is the type of association using the id from the
    TypeCodes table.

As the expected primary use for this is to create a new relationship
for an existing customers with a new customer, the relationship inputs 
the new customer in the Customer2 field.
For example, if the new customer is an Accountant for the existing
customer the Associations table will be updated as
Customer1 = Existing Customer
Association = Accountant
Customer2 = New Customer
*/

CREATE PROCEDURE CreateNewCustomerAndAssociation
       @NewCustomerName       varchar(50), -- The name of the new customer
       @NewCustomerTypeCodeId int,         -- The Type Code of the new customer
       @ExistingCustomerId  int,         -- The id of the existing customer
       @AssociationCodeId     int          -- The id code of the association type between customers
AS

INSERT INTO Customers (CustomerName, TypeCodeId)
VALUES (@NewCustomerName, @NewCustomerTypeCodeId)

INSERT INTO Associations (Customer1Id, TypeCodeId, Customer2Id)
VALUES (@ExistingCustomerId, @AssociationCodeId, SCOPE_IDENTITY())
;



/*
This procedure DeleteCustomer is used to delete an existing customer.

To do so, first any associations which include the customer are deleted, 
then any securities on accounts belonging to the customer are deleted,
then any accounts belonging to the customer are deleted,
finally the customer info in the customer database is deleted.
*/

CREATE PROCEDURE DeleteCustomer
       @CustomerId int -- This is the id code of the customer being deleted
AS

DELETE FROM Associations
 WHERE @CustomerId IN (Customer1Id, Customer2Id)

DELETE S
  FROM Securities AS S
       INNER JOIN Accounts AS A
       ON S.AccountID = A.AccountId
 WHERE @CustomerId = A.CustomerId       

DELETE FROM Accounts
 WHERE CustomerId = @CustomerId

DELETE FROM Addresses
 WHERE CustomerId = @CustomerId

DELETE FROM Customers
 WHERE CustomerID = @CustomerID
;


/*
The procedure DeleteTypeCode is used to 'soft' delete an
entry in the TypeCode table.
To soft delete a TypeCode we amend the IsActive field to 0.
This indicates that particular code is no longer in use.
*/

CREATE PROCEDURE DeleteTypeCode
       @TypeCodeId int -- This is the TypeCodeId of the code being deleted
AS

UPDATE TypeCodes
   SET TypeCodeActive = 0
 WHERE TypeCodeId = @TypeCodeId
;

/*
Deleted reference data view.
This data view will show all the entries from the DataCodes table which
have been deleted using the DeleteTypeCode procedure.
This shows all TypeCodes where TypeCodeActive is 0, which indicates
the entry has been soft deleted.

*/

CREATE VIEW vwDeletedTypes
AS
SELECT TypeCodeId, TypeCodeName, TypeCodeCategory, TypeCodeActive
  FROM TypeCodes
 WHERE TypeCodeActive = 0
;
 

/*

The view vwCustomerAssociations is used to view all associations
between all customers. This returns the full list of associations
from the associations table renaming the customers based on the
name in the customer table and the association type based on the 
description in the datatype table.
To show the association both ways, the associations are presented
a second time with the order of relationship reversed.

*/

CREATE VIEW vwCustomerAssociations
AS

SELECT C1.CustomerName +
       ' has ' + T.TypeCodeName +
       ' who is ' + C2.CustomerName + '.'
       AS Associations
  FROM Associations AS A  
       INNER JOIN Customers AS C1
       ON A.Customer1Id = C1.CustomerId
       INNER JOIN TypeCodes AS T
       ON A.TypeCodeId = T.TypeCodeId  
       INNER JOIN Customers AS C2
       ON A.Customer2Id = C2.CustomerId       

UNION ALL

SELECT C2.CustomerName +
       ' is the ' + T.TypeCodeName +
       ' for ' + C1.CustomerName + '.'
       AS Associations
  FROM Associations AS A  
       INNER JOIN Customers AS C1
       ON A.Customer1Id = C1.CustomerId
       INNER JOIN TypeCodes AS T
       ON A.TypeCodeId = T.TypeCodeId  
       INNER JOIN Customers AS C2
       ON A.Customer2Id = C2.CustomerId
;

/* EOF */
