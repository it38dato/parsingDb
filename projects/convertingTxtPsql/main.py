import os
import shutil
import subprocess
from datetime import datetime

count = 0
DB_HOST = "192.168.122.128"
DB_NAME = "tbase2"
DB_USER = "tuser"
DB_PASSWORD = "tpassword"
listLines = []
listHomeDir = []
listEnvDir = []

homeDir = os.path.expanduser("~")
print(homeDir)
currDir = os.getcwd()
print(currDir)
listHomeDir = os.listdir(homeDir)
print(listHomeDir)
os.chdir(homeDir)
print(f"Перешли в каталог: {os.getcwd()}")
if "envTxtPsql" not in listHomeDir:
	print("- В домашней директории отсутствует папка: " + "envTxtPsql" + ". Сейчас настроится данная папка. Запустите Активацию командой source envTxtPsql/bin/activate перед повторным запуском скрипта *.py")
	result = subprocess.run(["python3 -m venv "+"envTxtPsql"], shell=True)
	print(result.stdout)
	try:
	    result = subprocess.run(
	        ["source "+"envTxtPsql"+"/bin/activate && pip install -r "+currDir+"/requirements.txt"],
	        shell=True,
	        check=True,
	        capture_output=True,
	        text=True,
	        executable='/bin/bash',
	        env=os.environ.copy()
	    )
	    print("Установка завершена успешно!")
	    print("Стандартный вывод:", result.stdout)
	except subprocess.CalledProcessError as err:
	    print("Произошла ошибка при установке.")
	    print("Код возврата:", err.returncode)
	    print("Стандартный вывод:", err.stdout)
	    print("Стандартная ошибка:", err.stderr)
os.chdir(currDir)
print(f"Перешли в каталог: {os.getcwd()}")

try:
	import psycopg2
	from psycopg2.extras import execute_values
except ModuleNotFoundError:
	print("Запустите Активацию командой source envTxtPsql/bin/activate перед повторным запуском скрипта *.py")

def create_table_if_not_exists():
    conn = None
    try:
        # Подключение к базе данных PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        # SQL-запрос для создания таблицы IF NOT EXISTS| RU | GE | TGE | EN | TEN | Content |
        create_table_query = """
            CREATE TABLE IF NOT EXISTS guide3 (
                id SERIAL PRIMARY KEY,
                RU TEXT,
                GE TEXT,
                TGE TEXT,
                EN TEXT,
                TEN TEXT,
                Content TEXT
            );
        """
        # Выполнение запроса
        cur.execute(create_table_query)        
        # Фиксация изменений в базе данных
        conn.commit()
        print("Таблица успешно создана или уже существует.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
    finally:
        # Закрытие соединения
        if conn is not None:
            conn.close()

def insert_to_postgresql(records):
    conn = None
    try:
        # Подключение к базе данных PostgreSQL
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cur = conn.cursor()
        # SQL-запрос для вставки данных в указанные столбцы
        columns = "ru, ge, tge, en, ten, content"
        insert_query = f"INSERT INTO guide3 ({columns}) VALUES %s"        
        # Преобразование списка списков в список кортежей
        # (execute_values работает с итерируемыми объектами)
        records_as_tuples = [tuple(row) for row in records]        
        # Используем execute_values для эффективной массовой вставки
        execute_values(cur, insert_query, records_as_tuples)        
        # Фиксация изменений в базе данных
        conn.commit()
        print(f"{cur.rowcount} записей успешно вставлено в таблицу 'guide3'.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Ошибка: {error}")
        #sys.exit(1)
    finally:
        # Закрытие соединения
        if conn is not None:
            conn.close()

#print("+ Add file (logOutPy.log)\n")
with open("logOutPy.log", "w") as outfile:
	outfile.write("+ Add file (logOutPy.log)\n")

with open("textDictionary.txt", "r") as file:
	for line in file:
		#count = count+1
		#print(str(count) +" - "+ line.strip())
		#with open("logOutPy.log", "a") as outfile:
		#	outfile.write("+ Add objects (count, line)\n")

		#print(type(line.strip()))
		listLine = (line.strip()).split("|")
		#print(listLine)
		with open("logOutPy.log", "a") as outfile:
			outfile.write("+ Add list (listLine)\n")

		#print(listLine[1])
		#print(listLine[2])
		#print(listLine[3])
		#print(listLine[4])
		#print(listLine[5])
		#print(listLine[6])
		#print(listLine[7])
		#print(listLine[1:7])
		listLines.append(listLine[1:7])
#print(listLines)
with open("logOutPy.log", "a") as outfile:
	outfile.write("+ Add list (listLines)\n")

if __name__ == "__main__":
    create_table_if_not_exists()
    insert_to_postgresql(listLines)