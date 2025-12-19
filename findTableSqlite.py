import sqlite3
import pandas as pd
from libs.importKeys import importDataFile

def list_tables_with_pandas(db_file):
    conn = sqlite3.connect(db_file)    
    query = "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    df = pd.read_sql_query(query, conn)    
    conn.close()
    
    if not df.empty:
        print("\nСписок таблиц (через pandas):")
        print(df['name'].tolist())
    else:
        print("\nВ базе данных нет пользовательских таблиц.")

def list_tables_sqlite(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()        
        print(f"Подключено к базе данных: {db_file}")

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")        
        tables = cursor.fetchall()
        
        if tables:
            print("\nСписок таблиц в базе данных:")
            for table in tables:
                # fetchall() возвращает список кортежей [(table_name,), ...]
                print(f"- {table[0]}")
        else:
            print("\nВ базе данных нет пользовательских таблиц.")

    except sqlite3.Error as e:
        print(f"Произошла ошибка базы данных: {e}")
    finally:
        if conn:
            conn.close()
            print("Соединение с БД закрыто.")

def display_table_site_with_pandas(db_file):
    listDataFile = importDataFile([])
    count = 0
    for index in listDataFile:
        print(str(count)+" - "+index)
        count = count + 1

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        table_name = listDataFile[25]
        query = f"SELECT * FROM [{table_name}]"
        df = pd.read_sql_query(query, conn)
        
        if not df.empty:
            print(f"Данные из таблицы '{table_name}':")
            print(df)
        else:
            print(f"Таблица '{table_name}' пуста или не найдена.")

    except sqlite3.Error as e:
        print(f"Произошла ошибка базы данных: {e}")
    except pd.io.sql.DatabaseError as e:
        print(f"Ошибка pandas при выполнении запроса: {e}")
    finally:
        if conn:
            conn.close()
            print("\nСоединение с БД закрыто.")

def display_table_site_without_pandas(db_file):
    listDataFile = importDataFile([])
    count = 0
    for index in listDataFile:
        print(str(count)+" - "+index)
        count = count + 1

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        table_name = listDataFile[25]
        print(f"Подключено к базе данных. Извлечение данных из таблицы '{table_name}'...")

        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        
        if records:
            column_names = [description[0] for description in cursor.description]
            
            print("-" * 50)
            print(f"Данные из таблицы '{table_name}':")
            print(" | ".join(column_names))
            print("-" * 50)
            
            for row in records:
                print(" | ".join(map(str, row)))
            print("-" * 50)
        else:
            print(f"Таблица '{table_name}' пуста или не найдена.")

    except sqlite3.Error as e:
        print(f"Произошла ошибка базы данных: {e}")
    finally:
        if conn:
            conn.close()
            print("Соединение с БД закрыто.")

database_file_path = 'db.sqlite3'
list_tables_with_pandas(database_file_path)
list_tables_sqlite(database_file_path)
display_table_site_with_pandas(database_file_path)
display_table_site_without_pandas(database_file_path)