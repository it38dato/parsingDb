import os
def importDataFile(listDataFile):
    file = "config.txt"
    def readFile(path):
        listDataInFunc = []
        if not os.path.exists(path):
            print(f"Ошибка: Файл {path} не найден.")
            return None, False
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                #content = f.read()
                #print(content)

                for line in f:
                    # line содержит символ новой строки "\n" в конце, 
                    # используйте rstrip() для его удаления
                    nullLine = line.strip()
                    #nullLine = line.rstrip() 
                    if nullLine and not nullLine.startswith("#"):
                        #print(nullLine)

                        # 3. Разделяем строку по первому вхождению знака "="
                        listDataLineFile = nullLine.split("=", 1)
                        #print(listDataLineFile)
                        if len(listDataLineFile) == 2:
                            # listDataLineFile[0] это строка "IPSERVER "
                            # listDataLineFile[1] это строка " 10.7..1 2.=1"
                            listKey = listDataLineFile[0].strip()   # Ключ (например, "IPSERVER") Применяем .strip() к первому элементу
                            listValue = listDataLineFile[1].strip() # Значение (например, "10.7..1 2.=1")  Применяем .strip() ко второму элементу
                            # 4. Добавляем ключ и значение по очереди в общий список
                            listDataInFunc.append(listKey)
                            listDataInFunc.append(listValue)
            return listDataInFunc, True
        
        #except FileNotFoundError:
        #    print(f"Ошибка: файл {path} не найден.")
        except Exception as e:
            print(f"Произошла ошибка при чтении файла {path}: {e}")
            return None, False

    listDataFile, boolStatus = readFile(file)
    if not boolStatus:
        print(f"Не удалось найти файл по пути: {os.path.abspath(file)}")
        pathNew = input("Пожалуйста, введите имя проекта или полный путь к файлу config.txt: ").strip()
        listDataFile, boolStatus = readFile(pathNew)
        if not boolStatus:
            print("Повторная попытка чтения не удалась. Возврат None.")
            return None
    return listDataFile

#listDataFile = importDataFile([])
#if listDataFile:
#    print(listDataFile)
