from importKeys import importDataFile

listDataFile = importDataFile([])
if listDataFile:
    print("Конфигурационные данные успешно загружены:")
    print(listDataFile)
else:
    print("Не удалось загрузить конфигурацию.")
# Пример, как можно извлечь данные из списка (если он всегда упорядочен парами ключ/значение)
if listDataFile and len(listDataFile) >= 2:
    testVar1 = listDataFile[1]
    print(f"Первый IP сервера: {testVar1}")