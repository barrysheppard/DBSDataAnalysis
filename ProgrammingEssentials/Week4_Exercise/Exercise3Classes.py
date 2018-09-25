# Week 4 Exercise 3


# Create a Class called Association
class Association():

    __newCustomerName = None
    __customerId1 = None
    __customerId2 = None
    __associationTypeId = None

    # Create Public properties (getters and setters) for the mandatory (not
    # nullable) columns on your Associations table. All the member variables
    # should be private and should only be accessed via the Public Properties.

    # lets do an __init__ to make things easier.

    def __init__(self, customerName, cusId1, cusId2, assocTypeId):
        self.__newCustomerName = customerName
        self.__customerId1 = cusId1
        self.__customerId2 = cusId2
        self.__associationTypeId = assocTypeId

    def SetName(self, newCustomerName):
        self.__newCustomerName = newCustomerName

    def SetCustomer1(self, customerId1):
        self.__customerId1 = customerId1

    def SetCustomer2(self, customerId2):
        self.__customerId2 = customerId2

    def SetAssociationType(self, associationTypeId):
        self.__associationTypeId = associationTypeId

    def GetName(self):
        return self.__newCustomerName

    def GetCustomer1(self):
        return self.__customerId1

    def GetCustomer2(self):
        return self.__customerId1

    def GetAssociationTypeId(self):
        return self.__associationTypeId

    # Create a method called CreateAssociation with the following pramaters:
    # self, customerId2, associationTypeId

    # Note: I'm changing this. I want to create it in the object and then
    # use this function to commit. It doesn't really make sense to me
    # otherwise

    def CreateAssociation(self):

        # Within the CreateAssociation function call the Stored Procedure
        # you implementsin the last module to create the association.

        import pypyodbc

        try:
            # 1 Define the Database Connection
            dbConnection = pypyodbc.connect("Driver={SQL Server};"
                                            "Server=localhost;"
                                            "Database=DBS_RetailBanking;")

            # 2 Define the SQL Command
            sqlCommand = "{CALL uspCreateAssociation (?, ?,?,?)}"

            # 3 Define parameter values
            parameters = [self.__newCustomerName, self.__customerId1,
                          self.__customerId2, self.__associationTypeId]

            # 3 Replace Parameter Placeholders and Execute Command
            cursor = dbConnection.cursor()
            cursor.execute(sqlCommand, parameters)

            # 4 Commit Changes
            dbConnection.commit()

        except ConnectionError as ex:
            raise ex
        except Exception as ex:
            raise ex
        finally:
            # 5 Close Database Connection
            if(dbConnection is not None):
                dbConnection.close()

# Create a sperated PY file in visual studio where you will call the Class from
# -- continued in Exercise3Main.py
