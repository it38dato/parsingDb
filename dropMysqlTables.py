import mysql.connector
from libs.importKeys import importDataFile

listDataFile = importDataFile([])
count = 0
for index in listDataFile:
    print(str(count)+" - "+index)
    count = count + 1

try:
    connection = mysql.connector.connect(
        host=listDataFile[7],
        user=listDataFile[3],
        password=listDataFile[5],
        database=listDataFile[9]
    )

    if connection.is_connected():
        cursor = connection.cursor()
        #tables_to_drop = "nokia_site, nokia_mrbts, nokia_bcf, nokia_bts, nokia_trx, nokia_wcel, nokia_lncel, nokia_hwSran, nokia_hw2g, nokia_ethlk, nokia_lapd, nokia_cablink, nokia_gnbcf, nokia_add"
        tables_to_drop = listDataFile[15]
        sql_drop_command = f"DROP TABLE IF EXISTS {tables_to_drop};"
        cursor.execute(sql_drop_command)
        print(f"Таблицы '{tables_to_drop}' были удалены.")
        connection.commit() # Подтверждение изменений

except mysql.connector.Error as e:
    print(f"Ошибка при подключении к MySQL: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Соединение с MySQL закрыто.")