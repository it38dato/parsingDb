import mysql.connector
from libs.importKeys import importDataFile

listDataFile = importDataFile([])
count = 0
for index in listDataFile:
    print(str(count)+" - "+index)
    count = count + 1

listCmd = [
    "Показать список БД (1)",
    "Показать Список таблиц во всей БД (2)", 
    "Найти объект во всей базе и во всех таблицах (3)",
    "Выйти (0)"
    ]

while True:
    print("Список доступных команд:\n ", listCmd)
    choiceCmd = input("Выполните действия: ")
    print(f"... Выбор действия {choiceCmd}\n")

    choiceDB = input("Выберите БД (Nokia / Ericsson / Django): ")
    print(f"... Выбор БД {choiceDB}\n")

    match choiceDB:
        case "Nokia":
            print("+ Выбрана БД Nokia")

            conn = mysql.connector.connect(
                    host=listDataFile[23],
                    user=listDataFile[17],
                    password=listDataFile[19],
                )
            cursor = conn.cursor()
        case "Ericsson":
            print("+ Выбрана БД Ericsson")

            conn = mysql.connector.connect(
                    host=listDataFile[21],
                    user=listDataFile[17],
                    password=listDataFile[19],
                )
            cursor = conn.cursor()
        case "Django":
            print("+ Выбрана БД DjangoTemplate")

            conn = mysql.connector.connect(
                    host=listDataFile[7],
                    user=listDataFile[3],
                    password=listDataFile[5],
                )
            cursor = conn.cursor()
        
        case _:
            print("- Incorrect actions!")
            break

    match choiceCmd:
        case "1":
            print("+ Выполнение действия 1")
          
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            print("+ Получен список БД")
            print(databases)
        case "2":
            print("+ Выполнение действия 2")

            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            for db_tuple in databases:
                database = db_tuple[0]    
                cursor.execute(f"USE {database}")
                cursor.execute("SHOW TABLES")
                tables = [table[0] for table in cursor.fetchall()]
                print(f"Tables Name: {tables}; Database Name: {database}")
        case "3":
            print("+ Выполнение действия 3")
            obj = input("Выберите объект, который необходимо найти: ")
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            for db_tuple in databases:
                database = db_tuple[0]    
                cursor.execute(f"USE {database}")
                #print(database)
                cursor.execute("SHOW TABLES")
                tables = [table[0] for table in cursor.fetchall()]
                for table in tables:
                    try: 
                        listField = []
                        cursor.execute(f"SHOW COLUMNS FROM {table}")
                        #print(table)
                        for (Field, Type, Null, Key, Default, Extra) in cursor:
                            listField.append(Field)
                        for col in listField:
                            cursor.execute("SELECT * FROM "+database+"."+table+" WHERE "+col+" LIKE '%"+obj+"%';")
                            found_objects = cursor.fetchall()
                            for row in found_objects:
                                 if obj in row:
                                    print(row)
                                    print(f"Колонка {col} в таблице {table} из базы {database}")
                    except mysql.connector.errors.DatabaseError:
                        continue
        case "0":
            break
        case _:
            print("- Incorrect actions!")

    choiceContinue = input("Do you wish to continue? [y/n]: ").lower()
    print(f"... Выбор действия {choiceContinue}")
    #print(choiceContinue)

    while choiceContinue not in ['y', 'n']:
        choiceContinue = input("- Invalid input! Enter y/n: ").lower()
    if choiceContinue in ['y']:
        state = 2 
    elif choiceContinue in ['n']:
        break

    cursor.close()
    conn.close()