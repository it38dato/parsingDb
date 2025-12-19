import os
import shutil
import glob
def replace(inputDir, outputDir):
    # Убедимся, что исходная папка существует
    if not os.path.exists(inputDir):
        print(f"Ошибка: Исходная папка не найдена: {inputDir}")
        exit()

    # Убедимся, что целевая папка существует, или создадим ее
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
        print(f"Целевая папка создана: {outputDir}")

    # 1. Получаем список всех файлов в исходной папке (полные пути)
    # Используем glob.glob для получения списка файлов
    files = glob.glob(os.path.join(inputDir, '*'))

    # Отфильтровываем только файлы (исключаем подпапки, если они есть)
    files = [f for f in files if os.path.isfile(f)]

    if not files:
        print("В исходной папке нет файлов для перемещения.")
        exit()

    # 2. Сортируем файлы по дате изменения (от старых к новым)
    # os.path.getmtime(f) возвращает время последнего изменения файла в виде временной метки (timestamp)
    files.sort(key=os.path.getmtime)

    # Самый свежий файл будет последним в отсортированном списке
    latest_file = files[-1]
    files_to_move = files[:-1] # Все файлы, кроме последнего

    print(f"Всего найдено файлов: {len(files)}")
    print(f"Самый свежий файл (останется): {os.path.basename(latest_file)}")
    print(f"Файлов для перемещения: {len(files_to_move)}")

    # 3. Перемещаем файлы
    for file_path in files_to_move:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(outputDir, file_name)
        try:
            shutil.move(file_path, destination_path)
            print(f"Перемещен: {file_name}")
        except shutil.Error as e:
            print(f"Ошибка перемещения файла {file_name}: {e}")
        except OSError as e:
            print(f"Ошибка ОС при перемещении файла {file_name}: {e}")
    return inputDir, outputDir
#SOURCE_DIR, DEST_DIR = replace(f'{listDataFile[17]}', f'{listDataFile[23]}')
#SOURCE_DIR, DEST_DIR = replace(f'{listDataFile[19]}', f'{listDataFile[25]}')
#SOURCE_DIR, DEST_DIR = replace(f'{listDataFile[21]}', f'{listDataFile[27]}')
#print("Перемещение завершено.")