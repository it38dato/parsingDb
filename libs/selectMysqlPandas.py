import mysql.connector
import pandas as pd
from mysql.connector import Error

def display_table_site_with_pandas(fromExcel, df, hostSql, userSql, passwdSql, dbSql):
    conn = None
    listExcelLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR"]
    
    #listDataFile = importDataFile([])
    #count = 0
    #for index in listDataFile:
    #    print(str(count)+" - "+index)
    #    count = count + 1

    try:
        # Установление соединения
        conn = mysql.connector.connect(
            host=hostSql,
            user=userSql,
            password=passwdSql,
            database=dbSql
        )

        if conn.is_connected():
            print("Соединение с базой данных установлено успешно.")            
            # SQL-запрос, который мы хотим выполнить
            query = f"SELECT * FROM {fromExcel}"            
            # Использование pandas.read_sql_query для загрузки данных напрямую в DataFrame
            df = pd.read_sql_query(query, conn)
            df.columns = listExcelLetters[0:len(df.columns)]
            print(f"\nДанные успешно загружены в DataFrame. Получено строк: {len(df)}")

    except Error as e:
        print(f"Ошибка при работе с MySQL: {e}")
    finally:
        # Закрытие соединения
        if conn is not None and conn.is_connected():
            conn.close()
            print("Соединение с MySQL закрыто.")
    return fromExcel, df, hostSql, userSql, passwdSql, dbSql
#listDataFile = importDataFile([])
#dfSheet, dfSite = display_table_site_with_pandas(listDataFile[25], pd.DataFrame())
#print(dfSite)