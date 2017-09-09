from helpers import * 


coffee = loadData("data/c484 Data - Coffee.csv");
inventory = loadData("data/c484 Data - Inventory.csv");
ordersBySales = loadData("data/c484 Data - OrdersBySalesPersons.csv");
salespeople = loadData("data/c484 Data - SalesPersons.csv");

tablesList = [];



######################################################################
## Employee Table
##########################
tableName = "Employee";
columns = ['EmpNum','Name'];
data = pd.DataFrame(salespeople, columns=columns).drop_duplicates();
data.columns = ['EmpID', 'Name'];

additionalData = [
    ['EMP0000', 'Bob Bureaucrat'], 
    ['EMP0101', 'Sam Supervison'], 
    ['EMP0102', 'Mary Manager'], 
    ['EMP0103', 'Fred Foreman'],
]
data2 = pd.DataFrame(additionalData, columns = data.columns);
data = data.append(data2);

#print(data);
tablesList.append({'tableName' : tableName, 'data' : data});  



######################################################################
## Retailer Table
##########################
tableName = "Retailer";
columns = ['RetID','Name.2','Location'];
data = pd.DataFrame(coffee, columns=columns).drop_duplicates();
data.columns = ['RetID','Name','Location'];

##print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  



######################################################################
## SalesPerson Table
##########################
tableName = "SalesPerson";
columns = ['EmpNum','RetailID','StartDate','EndDate'];
data = pd.DataFrame(salespeople, columns=columns).drop_duplicates();
data.columns = ['EmpID', 'RetID', 'StartDate', 'EndDate'];

#print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  




######################################################################
## Blend Table
##########################
tableName = "Blend";
columns = ['BlnID','Name.1','Type', '$/lb', 'Gnd', 'RetID'];
data = pd.DataFrame(coffee, columns=columns).drop_duplicates();
data.columns = ['BlendID','Name','Type', 'PricePerLB', 'Gnd', 'RetID'];

##print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  


######################################################################
## CoffeeType Table
##########################
tableName = "CoffeeType";
columns = ['CoffeeTypeID', 'Description'];
data = pd.DataFrame([["1", "Decaf"], ["0", "Regular"]], columns=columns);

##print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  


######################################################################
## Bean Table
##########################
tableName = "Bean";
columns = ['BeanID','Name.3','Origin', 'DateSto', 'Amt', 'Cost', 'Decaf'];
data = pd.DataFrame(coffee, columns=columns).drop_duplicates();
data.columns = ['BeanID','Name','Origin', 'DateSto', 'Amt', 'Cost', 'CoffeeTypeID'];

##print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  

######################################################################
## Recipies Table
##########################
tableName = "Recipes";
columns = ['BlnID','BeanID','%'];
data = pd.DataFrame(coffee, columns=columns).drop_duplicates();
data.columns = ['BlendID', 'BeanID', 'Percentage'];

#print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  



######################################################################
## Customer Table
##########################
tableName = "Customer";
columns = ['Cust#','Name','Addr'];
data = pd.DataFrame(coffee, columns=columns).drop_duplicates();
data.columns = ['CustID', 'Name', 'Address'];

#print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  



######################################################################
## Orders Table
##########################
tableName = "Orders";
columns = ['Ord#','Date','Cust#', 'Ship', 'Ship$'];
data = pd.DataFrame(coffee, columns=columns).drop_duplicates();
data.columns = ['OrderID', 'Date', 'CustID', 'Carrier', 'ShippingCost'];

columns = ['OrderNum','Date','CustID', 'ShipMode', 'ShiCost'];
data2 = pd.DataFrame(inventory, columns=columns).drop_duplicates();
data2.columns = ['OrderID', 'Date', 'CustID', 'Carrier', 'ShippingCost'];
data = data.append(data2).drop_duplicates();
#print (data);

#####
## Add EmpID to Orders - not trivial since there are two bill browns 
#####
## Associate salesNames with orders
columns = ['OrderNumber', 'Salesperson'];
OrdersWithSalesPersonNames = pd.DataFrame(ordersBySales, columns=columns).drop_duplicates();
OrdersWithSalesPersonNames.columns = ['OrderID', 'Name'];
##print(OrdersWithSalesPersonNames);

## Associate Order Numbers with Store ID
## by Select RetID where CoffeeShipments.OrderID = OrdersWithSalesPersonNames.OrderID and CoffeeShipments.BlendID = Blend.BlendID 
columns = ['Ord#','RetID'];
OrderNumbersWithRetIDs = pd.DataFrame(coffee, columns=columns).drop_duplicates();
OrderNumbersWithRetIDs.columns = ['OrderID', 'RetID'];

OrdersWithSalesPersonNamesAndRetIDs = OrdersWithSalesPersonNames.merge(OrderNumbersWithRetIDs, on = 'OrderID', how = 'left');
##print(OrdersWithSalesPersonNamesAndRetIDs);

## Associate Employees with Sales name and retailer
columns = ['EmpNum','Name','RetailID'];
EmployeesWithNameAndRetailer = pd.DataFrame(salespeople, columns=columns).drop_duplicates();
EmployeesWithNameAndRetailer.columns = ['EmpID', 'Name', 'RetID'];

## Associate orders with empid 
## by Select EmpID where RetOrder.RetID = SalesPersonsWithNames.RetID AND OrdersWithSalesPersonNames.SalesName = SalesPersonsWithNames.Name
OrdersWithEmpID = OrdersWithSalesPersonNamesAndRetIDs.merge(EmployeesWithNameAndRetailer, on = ['RetID', 'Name'], how = 'left');
##print(OrdersWithEmpID);
columns = ['OrderID', 'EmpID'];
OrdersWithEmpID = pd.DataFrame(OrdersWithEmpID, columns=columns).drop_duplicates();
##print(OrdersWithEmpID);

## Finally add the data
data = data.merge(OrdersWithEmpID, on = ['OrderID'], how = 'left');

#print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  





######################################################################
## Product Table
##########################
tableName = "Product";
columns = ['InvNum','Desc','Cost','Wt'];
data = pd.DataFrame(inventory, columns=columns).drop_duplicates();
data.columns = ['InvID', 'Description', 'Cost', 'Wt'];

tablesList.append({'tableName' : tableName, 'data' : data});  



######################################################################
## ProductShipments Table
##########################
tableName = "ProductShipments";
columns = ['OrderNum','InvNum','Qty'];
data = pd.DataFrame(inventory, columns=columns).drop_duplicates();
data.columns = ['OrderID', 'InvID', 'Qty'];

#print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  



######################################################################
## Manager Table
##########################
tableName = "Manager";
columns = ['EmpID','RetID','StartDate','EndDate', 'LastAccess'];
data = [
    ['EMP0101', 'CBC1', '2016-06-03', np.nan, np.nan],
    ['EMP0102', 'NYC1', '2016-06-03', np.nan, np.nan],
    ['EMP0103', 'SFO3', '2016-06-03', np.nan, np.nan],
];
data = pd.DataFrame(data,  columns=columns).drop_duplicates();

##print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  



######################################################################
## CoffeeShipments Table
##########################
tableName = "CoffeeShipments";
columns = ['Ord#','BlnID','#lb'];
data = pd.DataFrame(coffee, columns=columns).drop_duplicates();
data.columns = ['OrderID', 'BlendID', 'NumLB'];

##print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  




######################################################################
## Bureaucrat Table
##########################
tableName = "Bureaucrat";
columns = ['EmpID','StartDate','EndDate','NextInspection'];
data = [
    ['EMP0000', np.nan, np.nan, np.nan],
];
data = pd.DataFrame(data,  columns=columns).drop_duplicates();

##print (data);
tablesList.append({'tableName' : tableName, 'data' : data});  




###########################################################################
## Output the data as SQL
###########################################################################
allInserts = "";
for i in range (0, len(tablesList)):
    thisElement = tablesList[i];
    thisTableName = thisElement['tableName'];
    thisTableData = thisElement['data'];
    theseColumns = thisTableData.columns.tolist();
    theseValues = thisTableData.values.tolist();

    #print(thisTableName);
    #print(thisTableData.columns.tolist());
    #print(thisTableData.values.tolist());
    
    theseInserts = (returnInsertStatements(thisTableName, theseColumns, theseValues));
    allInserts = allInserts + theseInserts + "\n";
    


with open("data_load.sql", "w") as text_file:
    text_file.write(allInserts)