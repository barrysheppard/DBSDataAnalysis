
/* 

For testing purposes these are in place to clean up    

*/

DROP TABLE Securities;
DROP TABLE Accounts;
DROP TABLE Addresses;
DROP TABLE Associations;
DROP TABLE Customers;
DROP TABLE TypeCodes;


CREATE TABLE TypeCodes (
       TypeCodeId       int         NOT NULL IDENTITY(1,1),
       TypeCodeName     varchar(50) NOT NULL, -- 
       TypeCodeCategory varchar(20) NOT NULL, -- Categories are Customers, Accounts, Security, Associations
       TypeCodeActive   bit         NOT NULL, -- 1 means the type is active, 0 means it is inactive
                        CONSTRAINT pk_TypeCodes PRIMARY KEY (TypeCodeId)
);

CREATE TABLE Customers (
       CustomerId   int         NOT NULL IDENTITY(1,1),
       CustomerName varchar(50) NOT NULL,
       TypeCodeId   int         NOT NULL, -- Customer types are Personal or Company
                    CONSTRAINT pk_Customers PRIMARY KEY (CustomerId),
                    CONSTRAINT fk_Customers_TypeCodes FOREIGN KEY (TypeCodeId)
                               REFERENCES TypeCodes(TypeCodeId)
);

/*
As all fields in an address are associated, for 3NF we separate them out into their own table
This allows us add multiple different addresses for one customer if required.
*/

CREATE TABLE Addresses (
       AddressId     int         NOT NULL IDENTITY(1,1),
       AddressLine1  varchar(50) NOT NULL,
       AddressLine2  varchar(50), -- Short addresses may only need the first line
       City          varchar(20) NOT NULL,
       StateProvince varchar(20), -- Provinces are not always needed
       PostCode      varchar(10), -- Some countries do not use postcodes
       Country       varchar(50) NOT NULL, 
       CustomerId    int         NOT NULL,  
                     CONSTRAINT pk_Addresses PRIMARY KEY (AddressId),
                     CONSTRAINT fk_Addresses_Customers FOREIGN KEY (CustomerId)
                                REFERENCES Customers(CustomerId)
);

CREATE TABLE Accounts (
       AccountId  int        NOT NULL IDENTITY(1,1),
       AccountNo  varchar(8) NOT NULL, -- not int as account numbers can start with 0
       Balance    money      NOT NULL, -- Current balance of the account
       OpenDate   datetime   NOT NULL, -- Date account is opened
       CustomerId int        NOT NULL, -- Customer who owns account
       TypeCodeId int        NOT NULL,
       AddressId  int        NOT NULL, -- The postal address for statements
                  CONSTRAINT pk_Accounts PRIMARY KEY (AccountId),
                  CONSTRAINT fk_Accounts_TypeCodes FOREIGN KEY (TypeCodeId)
                             REFERENCES TypeCodes(TypeCodeId),
                  CONSTRAINT uc_AccountNo UNIQUE (AccountNo)
);


CREATE TABLE Securities (
       SecuritiesId   int NOT NULL IDENTITY(1,1),
       SecuritiesDesc varchar(50),
       TypeCodeId     int NOT NULL,
       AccountId      int NOT NULL,
                      CONSTRAINT pk_Securities PRIMARY KEY (SecuritiesId),
                      CONSTRAINT fk_Securities_Accounts FOREIGN KEY (AccountId)
                                 REFERENCES Accounts(AccountId),
                      CONSTRAINT fk_Securities_TypeCodes FOREIGN KEY (TypeCodeId)
                                 REFERENCES TypeCodes(TypeCodeId)
);

CREATE TABLE Associations (
       AssociationId int NOT NULL IDENTITY(1,1),
       Customer1Id   int NOT NULL,
       TypeCodeId    int NOT NULL,
       Customer2Id   int NOT NULL,
                     CONSTRAINT pk_Assocations PRIMARY KEY (AssociationId),
                     CONSTRAINT fk_Associations_Customer1 FOREIGN KEY (Customer1Id)
                                REFERENCES Customers(CustomerId),
                     CONSTRAINT fk_Associations_Customer2 FOREIGN KEY (Customer2Id)
                                REFERENCES Customers(CustomerId),
                     CONSTRAINT fk_Associations_TypeCodes FOREIGN KEY (TypeCodeId)
                                REFERENCES TypeCodes(TypeCodeId),
                     CONSTRAINT uc_Association UNIQUE (Customer1Id, Customer2Id, TypeCodeId)
);
