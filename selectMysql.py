import pandas as pd
from libs.importKeys import importDataFile
from libs.selectMysqlPandas import display_table_site_with_pandas

listDataFile = importDataFile([])
count = 0
for index in listDataFile:
    print(str(count)+" - "+index)
    count = count + 1

dfSheet, dfSite, dbHost, dbUser, dbPasswd, dbName = display_table_site_with_pandas(listDataFile[25], pd.DataFrame(), listDataFile[7], listDataFile[3], listDataFile[5], listDataFile[9])
print(dfSite)