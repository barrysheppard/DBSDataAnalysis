
/*
The below includes some test data as part of the new database for Bank Corp Ltd client database.
*/


INSERT INTO TypeCodes (TypeCodeName, TypeCodeCategory, TypeCodeActive)
VALUES ('Personal Customer', 'Customers', 1),
       ('Corporate Customer', 'Customers', 1),
       ('Current Account', 'Accounts', 1),
       ('Deposit Account', 'Accounts', 1),
       ('Property', 'Securities', 1),
       ('Shares', 'Securities', 1),
       ('Accountant', 'Associations', 1),
       ('Investor', 'Associations', 1)
;

INSERT INTO Customers (CustomerName, TypeCodeId)
VALUES ('Voolia Ltd', 1),
       ('Rhyloo Inc', 1), 
       ('Katz Co.', 1),
       ('Realbuzz Ltd', 1),
       ('Thoughtblab', 1),
       ('Centimia Ltd', 1),
       ('Meezzy Co.', 1),
       ('Skibox Ltd', 1),
       ('Bluejam International', 1),
       ('Colman Solon', 2), 
       ('Clarey Joisce', 2),
       ('Eleni McClinton', 2),
       ('Ulrika Wolfe', 2),
       ('Saree Cominotti', 2),
       ('Gwenny Fallowes', 2),
       ('Gillian OGara', 2),
       ('Bel Silcock', 2),
       ('Philipa Dain', 2),
       ('Greggory Pitsall', 2),
       ('Lelah Stag', 2),
       ('Betteann Leivesley', 2)
;

INSERT INTO Addresses (AddressLine1, AddressLine2, City, StateProvince, PostCode, Country, CustomerId)
VALUES ('4038 Kropf Place', 'Point', 'Doña Remedios', null, '3009', 'Philippines', 3),
       ('94 Sundown Pass', 'Hill', 'Carolina', null, '65980-000', 'Brazil', 2),
       ('4120 Scofield Terrace', 'Park', 'Lypova Dolyna', null, null, 'Ukraine', 6),
       ('853 Sloan Pass', 'Avenue', 'Bantilan', null, null, 'Indonesia', 1),
       ('0 Petterle Point', 'Crossing', 'Zaoshi', null, null, 'China', 2),
       ('99 Lukken Way', 'Avenue', 'Kocēni', null, null, 'Latvia', 5),
       ('0 Atwood Plaza', 'Center', 'Bamusso', null, null, 'Cameroon', 2),
       ('3672 Thierer Hill', 'Parkway', 'Tongzha', null, null, 'China', 3),
       ('58 Talisman Trail', 'Alley', 'Tanggung', null, null, 'Indonesia', 6),
       ('201 Forest Point', 'Circle', 'Lin’an', null, null, 'China', 6)

INSERT INTO Accounts (AccountNo, Balance, OpenDate, CustomerId, TypeCodeId, AddressId)
VALUES ('12345678', 0, '1990-01-22', 1, 3, 2),
       ('00000001', 0, '2018-01-23', 2, 3, 4),
       ('11111111', 0, '1990-01-22', 1, 4, 6),
       ('80351703', 4617.81, '2017-11-30', 13, 5, 2),
       ('32302821', 3095.31, '2018-05-05', 19, 5, 7),
       ('51067234', 1127.94, '2017-06-26', 10, 5, 10),
       ('78599670', 7218.29, '2017-11-17', 16, 5, 6),
       ('61254470', 125.65, '2017-08-25', 16, 4, 2),
       ('84930570', 3480.50, '2018-05-14', 9, 5, 1),
       ('55886999', 5412.94, '2017-07-10', 20, 5, 8),
       ('35167087', 8876.35, '2017-11-28', 19, 4, 10),
       ('00000002', 0, '2018-01-23', 2, 4, 9)
;


INSERT INTO Securities (SecuritiesDesc, TypeCodeId, AccountId)
VALUES ('Flat 4, Avenue Drive', 1, 1),
       ('100 Shares in Apple', 2, 2)
;

INSERT INTO Associations (Customer1Id, TypeCodeId, Customer2Id)
VALUES (1, 7, 2), 
       (5, 8, 4),
       (3, 7, 2),
       (7, 8, 1),
       (5, 7, 4),
       (15, 8, 10),
       (11, 7, 8),
       (1, 8, 12),
       (10, 7, 2),
       (7, 8, 8),
       (1, 7, 14),
       (12, 8, 13)
;


/*
This data is to test constraints.
It should cause errors as it is creating duplicate entries.
*/

INSERT INTO Associations (Customer1Id, TypeCodeId, Customer2Id)
VALUES (1, 7, 2),
       (1, 7, 2)
;

INSERT INTO Accounts (AccountNo, Balance, OpenDate, CustomerId, TypeCodeId, AddressId)
VALUES ('11111111', 0, '1990-01-22', 1, 3, 3),
       ('11111111', 0, '1990-01-22', 1, 4, 4)
;


