INSERT INTO Employee (EmpID,Name) VALUES ('EMP108','Bill Brown');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP109','Jane Smith');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP202','Frank Martin');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP213','Anne Dough');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP303','Mike Green');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP309','Alice Grey');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP400','Bill Brown');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP0000','Bob Bureaucrat');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP0101','Sam Supervison');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP0102','Mary Manager');
INSERT INTO Employee (EmpID,Name) VALUES ('EMP0103','Fred Foreman');

INSERT INTO Retailer (RetID,Name,Location) VALUES ('CBC1','CBC Store','Indy, IN');
INSERT INTO Retailer (RetID,Name,Location) VALUES ('NYC1','New York 1','NYC, NY');
INSERT INTO Retailer (RetID,Name,Location) VALUES ('SFO3','SFO store','SFO, CA');

INSERT INTO SalesPerson (EmpID,RetID,StartDate,EndDate) VALUES ('EMP108','CBC1','2016-06-03',NULL);
INSERT INTO SalesPerson (EmpID,RetID,StartDate,EndDate) VALUES ('EMP109','NYC1','2016-06-03',NULL);
INSERT INTO SalesPerson (EmpID,RetID,StartDate,EndDate) VALUES ('EMP202','NYC1','2016-06-05',NULL);
INSERT INTO SalesPerson (EmpID,RetID,StartDate,EndDate) VALUES ('EMP213','CBC1','2016-05-10','2016-09-20');
INSERT INTO SalesPerson (EmpID,RetID,StartDate,EndDate) VALUES ('EMP303','SFO3','2016-06-10',NULL);
INSERT INTO SalesPerson (EmpID,RetID,StartDate,EndDate) VALUES ('EMP309','SFO3','2016-06-10',NULL);
INSERT INTO SalesPerson (EmpID,RetID,StartDate,EndDate) VALUES ('EMP400','SFO3','2016-07-10',NULL);

INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('CR01','Kona #1','R','80.5','G','CBC1');
INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('CR02','Kona #2','R','81.5','G','CBC1');
INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('CS03','Dark','S','49.5','G','CBC1');
INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('N02','Spec02','S','24.7','B','NYC1');
INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('CS05','House','S','17.0','G','CBC1');
INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('SFOP','Blend P','R','13.1','G','SFO3');
INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('CS04','SoAm','S','16.68','B','CBC1');
INSERT INTO Blend (BlendID,Name,Type,PricePerLB,Gnd,RetID) VALUES ('SFOA','Blend A','S','12.88','B','SFO3');

INSERT INTO CoffeeType (CoffeeTypeID,Description) VALUES ('1','Decaf');
INSERT INTO CoffeeType (CoffeeTypeID,Description) VALUES ('0','Regular');

INSERT INTO Bean (BeanID,Name,Origin,DateSto,Amt,Cost,CoffeeTypeID) VALUES ('K001','Kona #1','Kona, HI','May 2016','225','80.5','0');
INSERT INTO Bean (BeanID,Name,Origin,DateSto,Amt,Cost,CoffeeTypeID) VALUES ('K002','Kona #2','Kona, HI','May 2016','110','81.5','1');
INSERT INTO Bean (BeanID,Name,Origin,DateSto,Amt,Cost,CoffeeTypeID) VALUES ('B234','Brazil Dark','Santos, BR','Apr 2016','225','18.5','0');
INSERT INTO Bean (BeanID,Name,Origin,DateSto,Amt,Cost,CoffeeTypeID) VALUES ('CO23','Supremo','Columbia','Jun 2016','50','12.65','0');
INSERT INTO Bean (BeanID,Name,Origin,DateSto,Amt,Cost,CoffeeTypeID) VALUES ('P002','High Grown','Peru D','Jul 2016','100','13.1','1');
INSERT INTO Bean (BeanID,Name,Origin,DateSto,Amt,Cost,CoffeeTypeID) VALUES ('CR05','Tarrazu','Costa Rico','Jan 2015','33','14.8','0');
INSERT INTO Bean (BeanID,Name,Origin,DateSto,Amt,Cost,CoffeeTypeID) VALUES ('P001','High Grown','Peru','Jul 2016','100','13.1','0');

INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CR01','K001','100');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CR02','K002','100');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CS03','B234','50');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CS03','K001','50');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('N02','B234','90');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('N02','K001','10');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CS05','B234','75');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CS05','CO23','25');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('SFOP','P002','100');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CS04','B234','60');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CS04','CR05','20');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('CS04','P001','20');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('SFOA','CO23','50');
INSERT INTO Recipes (BlendID,BeanID,Percentage) VALUES ('SFOA','P001','50');

INSERT INTO Customer (CustID,Name,Address) VALUES ('AB101','John Doe','Indy');
INSERT INTO Customer (CustID,Name,Address) VALUES ('AC101','Anne Green','Indy');
INSERT INTO Customer (CustID,Name,Address) VALUES ('CC201','Bill Green','NYC');
INSERT INTO Customer (CustID,Name,Address) VALUES ('SS205','John Doe','SFO');
INSERT INTO Customer (CustID,Name,Address) VALUES ('LL101','Amy White','LA');
INSERT INTO Customer (CustID,Name,Address) VALUES ('QQ202','Gail Black','PHX');

INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('1012','2016-06-15','AB101','FedEx','4','EMP108');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('1013','2016-06-15','AC101','FedEx','8','EMP108');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('1015','2016-07-20','AC101','FedEx','4','EMP213');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('2000','2016-07-21','CC201','UPS','12','EMP109');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('2050','2016-08-01','SS205','UPS','16','EMP202');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('2051','2016-08-02','LL101','UPS','20','EMP108');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('2055','2016-08-10','QQ202','UPS','20','EMP303');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('3015','2016-08-10','AB101','UPS','12','EMP108');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('3016','2016-08-10','AB101','UPS','12','EMP309');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('3017','2016-08-10','LL101','FedEx','24','EMP400');
INSERT INTO Orders (OrderID,Date,CustID,Carrier,ShippingCost,EmpID) VALUES ('4000','2016-09-02','LL101','FedEx','32','EMP213');

INSERT INTO Product (InvID,Description,Cost,Wt) VALUES ('1345','CBC cup (W)','2.5','1');
INSERT INTO Product (InvID,Description,Cost,Wt) VALUES ('2208','CBC grinder','22.5','2');
INSERT INTO Product (InvID,Description,Cost,Wt) VALUES ('1346','CBC cup (B)','2.5','1');
INSERT INTO Product (InvID,Description,Cost,Wt) VALUES ('2209','AAA grinder','27.5','2');

INSERT INTO ProductShipments (OrderID,InvID,Qty) VALUES ('1013','1345','2');
INSERT INTO ProductShipments (OrderID,InvID,Qty) VALUES ('2000','2208','1');
INSERT INTO ProductShipments (OrderID,InvID,Qty) VALUES ('2050','1345','1');
INSERT INTO ProductShipments (OrderID,InvID,Qty) VALUES ('2050','1346','1');
INSERT INTO ProductShipments (OrderID,InvID,Qty) VALUES ('3015','2209','1');
INSERT INTO ProductShipments (OrderID,InvID,Qty) VALUES ('4000','2209','1');

INSERT INTO Manager (EmpID,RetID,StartDate,EndDate,LastAccess) VALUES ('EMP0101','CBC1','2016-06-03',NULL,NULL);
INSERT INTO Manager (EmpID,RetID,StartDate,EndDate,LastAccess) VALUES ('EMP0102','NYC1','2016-06-03',NULL,NULL);
INSERT INTO Manager (EmpID,RetID,StartDate,EndDate,LastAccess) VALUES ('EMP0103','SFO3','2016-06-03',NULL,NULL);

INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('1012','CR01','1');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('1013','CR02','1');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('1015','CS03','1');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('2000','N02','1');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('2050','N02','2');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('2051','CS05','5');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('2055','SFOP','5');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('3015','CS04','1');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('3016','SFOA','1');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('3017','SFOP','4');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('4000','CS05','4');
INSERT INTO CoffeeShipments (OrderID,BlendID,NumLB) VALUES ('4000','CR01','2');

INSERT INTO Bureaucrat (EmpID,StartDate,EndDate,NextInspection) VALUES ('EMP0000',NULL,NULL,NULL);

