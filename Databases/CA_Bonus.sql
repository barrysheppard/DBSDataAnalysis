/*

This is the optional code that I'll consider adding once the base code 
is up and running

*/


CREATE TABLE Companies (
       CompanyId   int         NOT NULL IDENTITY(1,1),
       CompanyName varchar(50) NOT NULL,
       TypeCodeId  int         NOT NULL,
       CustomerId  int         NOT NULL,
                   CONSTRAINT pk_Companies PRIMARY KEY (CompanyId),
                   CONSTRAINT fk_Companies_Customers FOREIGN KEY (CustomerId)
                              REFERENCES Customers(CustomerId),
                   CONSTRAINT fk_Companies_TypeCodes FOREIGN KEY (TypeCodeId)
                              REFERENCES TypeCodes(TypeCodeId)
);

CREATE TABLE PersonalCustomers (
       PersonalCustomersId int         NOT NULL IDENTITY(1,1),
       Forename            varchar(35) NOT NULL,
       Surname             varchar(35) NOT NULL,
       DateOfBirth         datetime    NOT NULL,
       CustomerID          int         NOT NULL,
                           CONSTRAINT pk_PersonalCustomers PRIMARY KEY (PersonalCustomersId),
                           CONSTRAINT fk_PersonalCustomers_Customers FOREIGN KEY (CustomerId)
                                      REFERENCES Customers(CustomerId)
);

/* 
The CustomersAccounts junction table allows an account owned by multiple customers.
For example in the case of a joint account.
*/

CREATE TABLE CustomersAccounts (
       CustomersAccountId int NOT NULL IDENTITY(1,1),
       CustomerId         int NOT NULL,
       AccountId          int NOT NULL,
                          CONSTRAINT pk_CustomersAccounts PRIMARY KEY (CustomersAccountId),
                          CONSTRAINT fk_CustomerId FOREIGN KEY (CustomerId)
                                     REFERENCES Customers(CustomerId),
                          CONSTRAINT fk_AccountId FOREIGN KEY (AccountId)
                                     REFERENCES Accounts(AccountId)
);
