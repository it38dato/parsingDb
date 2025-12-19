Task:
Необходимо написать скрипт который импортирует с excel в mysql
Decision:
для работы с проектом использую скрипты bat. 
Необходимо скачать Python (У меня 3.10) и установить ее. Затем уже использовать скрипты:
- checkPython.bat для проверки Python
- checkParsing.bat для настройки переменного окружения и создания проекта Parser. Скрипт попросит назвать проект, сохранит в домашнюю директорию папку envParserDB для работы с переменым окружения, добавит для проекта необходимые библиотеки записанные в файле requirements.txt, из файла config.txt добавит параметры прокси и сохранит папку с вашим названием проекта, откуда будет запускаться проект.
- startImportExcelMysql.bat для переноса данных с excel в mysql. Скрипт startImportExcelMysql.bat запускает проект importExcelMysql.py в домашней директории и считывает файлы с excel.
Все параметры необходимо подкорректировать в файл config.txt. в проекте должен находиться файл excel. с которого вы импортируете в базу данных.
- startDropMysqlTables.bat для удаления ненужных таблиц в базе. Скрипт startDropMysqlTables.bat запускает проект dropMysqlTables.py в домашней директории. В файле config.txt нужно заменить параметры БД и названия таблиц через запятую, которые вы ходите удалить.
Task:
Необходимо написать скрипт который находит информацию в БД mysql.
Decision:
для работы с проектом использую скрипты bat:
- startFindTableMysql.bat для поиска таблиц и объектов в БД mysql. Скрипт startFindTableMysql.bat запускает проект findTableMysql.py в домашней директории и запросит действия, которые необходимо сделать. Скрипт может показать список всех БД, список всех таблиц, которые находятся в БД и найти объект в выбраной БД. Необходимо в conifg.txt подключения БД  строки начиная с DB_ добавить свои параметры.
Task:
В проекте Django есть БД sqlte3. Необходимо проверить содержимое БД и добавить контент в БД.
Decision:
для работы с проектом использую скрипты bat:
- startfindTableSqlite.bat для поиска содержимого в БД Sqlite3. Для просмотра содержимого БД Sql используется скрипт findTableSqlite.py. скрипт покажет список таблиц БД в Sqlite3. Также нужно в файле config.txt в строке начиная FILTER_TABLE добавить таблицу, которую хотите найти. db.sqlite3 должен быть рядом с этим скриптом. 
- startAddTableSqlite.bat для добавления контента в Django, используя скрипт addTableSqlite.py. в файле addTableSqlite.py необходимо добавить свои параметры таблиц.
Task:
Есть инструмент Nokia написанный в VBA, который собирает данные по Nokia c Mysql. 
Добавить кнопку "Add 2100" и дописать макрос, который при нажатии на кнопку "Add 2100" дублирует из таблицы второй несущей LTE1800 и корректирует данные с таблицы параметры (Bandwidth, earfcnDL и LNHOIF / IRFIM instance 0).
Decision:
- в файле 4GCell_DataBuild_.xlsm необходимо снять защиту с листа и добавить возможность изменять код
Код:
Private Sub CommandButton3_Click()
    'MsgBox ("This is test code")
    Sheets("Main").Unprotect
    Range("A5:U7").Copy _
        Destination:=Range("A26:U28")
    Sheets("Main").Protect
    For Each cc In [I26:I28]
        Sheets("Main").Unprotect
        If cc.Value = "15" Then cc.Offset(, 0) = "10"
        Sheets("Main").Protect
    Next
    For Each cc In [K26:K28]
        Sheets("Main").Unprotect
        If cc.Value = "1875" Then cc.Offset(, 0) = "100"
        Sheets("Main").Protect
    Next
    For Each cc In [P26:P28]
        Sheets("Main").Unprotect
        If cc.Value = "100" Then cc.Offset(, 0) = "1875"
        Sheets("Main").Protect
    Next
    For Each cc In [J26:J28]
        lte2100 = cc + 40
       'MsgBox (lte2100)
        Sheets("Main").Unprotect
        If cc.Value = cc Then cc.Offset(, 0) = lte2100
        Sheets("Main").Protect
    Next
    'Sheets("Main").Protect
End Sub
Task:
Написать проект, который делает выполняет подключение к БД MySql и выгружает  таблицу из Mysql
Decision:
Проект работает в файле findInfo.xlsm
для настройки проекта:
- Visual Basic - Tools - References - +Microsoft ActiveX Data Objects 6.1 Library - ok
для запуска в файле findInfo.xlsm необходимо поменять параметры БД и режиме разработчика менять запросы.
Код:
Private Sub ConnectionDB()
    Dim oConn As Object
    Set oConn = New ADODB.Connection    
    oConn.Open "DRIVER={MySQL ODBC 8.0 Unicode Driver};Server=tipwindows;Database=tbase;User=tuser;Password=tpassword;PORT:3306;Option=3"
    If oConn.State = adStateOpen Then
        MsgBox "Connected! =)"
    End If
    Dim cmd As ADODB.Command  'переменная в которой будет запрос
    Set cmd = New ADODB.Command    
    Dim rec As ADODB.Recordset 'переменная в которой будет результат запроса
    Set rec = New ADODB.Recordset    
    Set cmd.ActiveConnection = oConn
    cmd.CommandText = "SELECT * FROM bss_2g_nokia" 'собственно, запрос
    cmd.CommandType = adCmdText
    cmd.Execute    
    Set rec.ActiveConnection = oConn
    rec.Open cmd    
    oConn.Close  
End Sub
- для запуска в файле findInfo.xlsm необходимо поменять параметры БД и в режиме разработчика менять запросы заменив строку SQLStr на запрос, который необоходимо выполнить
в Лист1 -отобразится информация после запуска кода.
Task:
В проекте 4GCell_DataBuild_.xlsm Не загружает таблицу из БД с таким запросом:
SELECT b.cellName as NSector
      ,SUBSTRING(CAST(b.cellName as CHAR),1,6) as SiteName
      ,bt.enbName as SystemModule
      , ROUND(POWER(10, e.pMAX/100)/1000,0) as Pmax               
      ,CAST((CAST(CAST(l.ulChBw AS CHAR) AS INT)/10) AS INT) AS Bandwidth                       
      ,l.LNCEL as CID       
      ,l.earfcnDL
      ,e.phyCellId AS PCI     
      ,l.rootSeqIndex      
      ,(CASE WHEN CAST(l.prachCS as CHAR) = '14' THEN '35(область)' ELSE '15(город)' END) AS CellRange
      ,e.tac as TAC  
      ,(CASE WHEN l.dlMimoMode = 0 THEN 'SingleTx' ELSE '' END) as SingleTx	  
FROM YOURDB1.LNCEL_begin b
  LEFT OUTER JOIN 
  (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD 
   UNION
   SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) l ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
  LEFT OUTER JOIN YOURDB1.LNCEL_end e ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL  
  LEFT OUTER JOIN YOURDB1.LNBTS_begin bt ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS
WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')
ORDER BY b.MRBTS, b.LNCEL
Decision:
Перед запуском необходимо проверить настройки листа:
- Excel - Рецензирование - Снять защиту с листа - пробовать обновить лист тем же запросом - за 25 минут загрузил и 26845 строк стало в таблице LIST - в LIST отобразились недостающие довесы
Алгортим:
- два вложенных запроса, проверьте сначала их по отдельности:
SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD 
SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD
- UNION Проверьте:
SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD 
UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD
- Составьте таблицу, которая получится после выполнения всех JOIN (можно проверять не все сразу, а добавлять по одному):
SELECT * FROM YOURDB1.LNCEL_begin AS b
- Запрос не выдал результат. командой show tables определил что изменилось название таблицы:
SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b
- следующий запрос:
SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b
LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD
UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l 
ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
- следующий запрос:
SELECT * FROM YOURDB1.LNCEL_end AS e
- Запрос не выдал результат. командой show tables определил что изменилось название таблицы:
SELECT * FROM YOURDB1_LNCEL.LNCEL_end AS e
- следующий запрос:
SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b
LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD
UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l 
ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
LEFT OUTER JOIN YOURDB1.LNCEL_end AS e 
ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL
- следующий запрос:
SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b
LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD
UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l 
ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e 
ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL
- следующий запрос:
SELECT * FROM YOURDB1.LNBTS_begin AS bt
- следующий запрос:
SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b
LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD
UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l 
ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e 
ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL
LEFT OUTER JOIN YOURDB1.LNBTS_begin AS bt 
ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS
- Посмотрите, есть ли в выводе поле b.cellName, соответствует ли оно вашему фильтру Where. Примените фильтр к запросу:
SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b
LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD
UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l 
ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e 
ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL
LEFT OUTER JOIN YOURDB1.LNBTS_begin AS bt 
ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS
WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')
ORDER BY b.MRBTS, b.LNCEL
- Уберите звёздочку, добавляйте по одному полю в выражение SELECT:
SELECT 
    l.LNCEL AS CID, 
    l.earfcnDL, l.rootSeqIndex, 
    CAST((CAST(CAST(l.ulChBw AS CHAR) AS INT)/10) AS INT) AS Bandwidth, 
    (CASE WHEN CAST(l.prachCS as CHAR) = '14' THEN '35(область)' ELSE '15(город)' END) AS CellRange,
    (CASE WHEN l.dlMimoMode = 0 THEN 'SingleTx' ELSE '' END) AS SingleTx, 
    b.cellName AS NSector, 
    SUBSTRING(CAST(b.cellName as CHAR),1,6) AS SiteName, 
    e.phyCellId AS PCI, 
    e.tac, 
    ROUND(POWER(10, e.pMAX/100)/1000,0) AS Pmax, 
    bt.enbName AS SystemModule
FROM YOURDB1_LNCEL.LNCEL_begin AS b
LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD
UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l 
ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e 
ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL
LEFT OUTER JOIN YOURDB1.LNBTS_begin AS bt 
ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS
WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')
ORDER BY b.MRBTS, b.LNCEL
- Общий результат по проверке запроса:
+SELECT 
+l.LNCEL, 
+l.earfcnDL, 
+l.rootSeqIndex, 
+CAST((CAST(CAST(l.ulChBw AS CHAR) AS INT)/10) AS INT), 
+(CASE WHEN CAST(l.prachCS as CHAR) = '14' THEN '35(область)' ELSE '15(город)' END), 
+(CASE WHEN l.dlMimoMode = 0 THEN 'SingleTx' ELSE '' END), 
+b.cellName, 
+SUBSTRING(CAST(b.cellName as CHAR),1,6), 
+e.phyCellId, 
+e.tac, 
+ROUND(POWER(10, e.pMAX/100)/1000,0), 
+bt.enbName
-FROM YOURDB1.LNCEL_begin AS b
+LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD
+UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l 
+ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL
-LEFT OUTER JOIN YOURDB1.LNCEL_end AS e 
+ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL
+LEFT OUTER JOIN YOURDB1.LNBTS_begin bt 
+ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS
+WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')
+ORDER BY b.MRBTS, b.LNCEL
- Убрал order BY для быстрого выполнения запроса
Task:
Написать скрипт в Python, который выполняет запросы с mysql
Decision:
для работы с проектом использую скрипты bat:
- startSelectMysql.bat для запуска проекта selectMysql.py. в Файле config.txt нужно заменить параметеры БД и FILTER_TABLE