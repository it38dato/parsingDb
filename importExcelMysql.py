import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import os
import re
from libs.importKeys import importDataFile

listDataFile = importDataFile([])
count = 0
for index in listDataFile:
    print(str(count)+" - "+index)
    count = count + 1

DB_USER = listDataFile[3]
DB_PASSWORD = listDataFile[5]
DB_HOST = listDataFile[7]
DB_NAME = listDataFile[9]
EXCEL_FILE = listDataFile[11]
TECHNOLOGY_PREFIX = listDataFile[13]

# Функция для обеспечения уникальности имен столбцов
#def make_columns_unique(df):
#    print(df)
#    cols = pd.Series(df.columns)
#    for dup in cols[cols.duplicated()].unique():
#        cols[cols[cols == dup].index.values.tolist()] = [dup + '_' + str(i) if i != 0 else dup for i, i in enumerate(range(sum(cols == dup)))]
#    df.columns = cols
#    return df

def import_excel_to_mysql_xlsb(excel_file, db_user, db_password, db_host, db_name, prefix_tech):
    engine = None
    try:
        db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"        
        engine = create_engine(db_url)
        excel_data = pd.read_excel(excel_file, sheet_name=None, engine='pyxlsb')

        for sheet_name, df in excel_data.items():
            # 1. Очистка имен столбцов (как раньше)
            df.columns = df.columns.str.replace(' ', '_', regex=False).str.replace(r'[^a-zA-Z0-9_]', '', regex=True)            
            # 2. ДОБАВЛЕНИЕ: Обеспечение уникальности имен столбцов
            #df = make_columns_unique(df)
            # 2. НОВОЕ РЕШЕНИЕ: Обеспечение уникальности имен столбцов с помощью pd.factorize
            # Это гарантирует, что дубликаты получат уникальный индекс, например, 'lac', 'lac_1', 'lac_2'
            df.columns = pd.factorize(df.columns)[0].astype(str) + '_' + df.columns
            # Удаляем дубликаты, которые могут появиться после factorize (например, при пустых именах столбцов)
            df = df.loc[:,~df.columns.duplicated()]
            # Очистка имени таблицы
            safe_sheet_name = re.sub(r'[^a-zA-Z0-9_]', '', sheet_name.replace(' ', '_'))
            table_name = f"{prefix_tech}_{safe_sheet_name}"  

            if table_name and safe_sheet_name:
                print(f"Импорт данных из листа '{sheet_name}' в таблицу '{table_name}'...")
                # При использовании if_exists='replace', старая таблица удаляется полностью перед созданием новой схемы.
                df.to_sql(name=table_name, con=engine, index=False, if_exists='replace')
                print(f"Таблица '{table_name}' успешно обновлена.")
            else:
                print(f"Пропущен лист с пустым или недопустимым именем: '{sheet_name}'")

    except ImportError:
        print("Ошибка: Не установлена библиотека 'pyxlsb'. Пожалуйста, выполните: pip install pyxlsb")
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к MySQL: {err}")
    except FileNotFoundError:
        print(f"Файл Excel не найден: {excel_file}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if engine:
        #if 'engine' in locals() and engine:
            engine.dispose()
if __name__ == "__main__":
    import_excel_to_mysql_xlsb(EXCEL_FILE, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, TECHNOLOGY_PREFIX)
