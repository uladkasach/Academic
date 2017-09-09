import pandas as pd
import numpy as np

def loadData(data_source):
    #######################
    ## Load Data
    #######################
    print('\nLoading Data...');
    data = pd.read_csv(data_source)
    
    if ( False ): ## Dev - Display Sample
        data = data[1:2];
        print(data);
        
    return data;

def returnOneInsertStatement(tableName, columnsListed, valuesListed):
    return "INSERT INTO " + tableName + " ("+columnsListed+") VALUES ("+valuesListed+");\n";   

def returnInsertStatements(tableName, columnNames, values):
    columnsListed = "";
    for i in range(0, len(columnNames)):
        thisColumnName = columnNames[i];
        if(i != 0):
            columnsListed = columnsListed + ",";
        columnsListed = columnsListed + "" + thisColumnName + "";
    
    fullString = "";
    for i in range(0, len(values)):
        valuesListed = "";
        for j in range(0, len(columnNames)):
            thisValue = values[i][j];
            if(pd.isnull(thisValue)):
                thisValueWrapped = "NULL";   
            else:
                thisValueWrapped = "'" + str(thisValue) + "'";
            if(j != 0):
                valuesListed = valuesListed + ",";
            valuesListed = valuesListed + thisValueWrapped;
        fullString += returnOneInsertStatement(tableName, columnsListed, valuesListed); 
    
    return fullString;

