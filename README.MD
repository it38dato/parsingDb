# Parsing DB
<p>
    <strong>Task:</strong><br>
    Необходимо написать скрипт который импортирует с excel в mysql<br>
    <strong>Decision:</strong><br>
    для работы с проектом использую скрипты bat.<br>
    Необходимо скачать Python (У меня 3.10) и установить ее. Затем уже использовать скрипты:<br>
    - checkPython.bat для проверки Python<br>
    - checkParsing.bat для настройки переменного окружения и создания проекта Parser. Скрипт попросит назвать проект, сохранит в домашнюю директорию папку envParserDB для работы с переменым окружения, добавит для проекта необходимые библиотеки записанные в файле requirements.txt, из файла config.txt добавит параметры прокси и сохранит папку с вашим названием проекта, откуда будет запускаться проект.<br>
    - startImportExcelMysql.bat для переноса данных с excel в mysql. Скрипт startImportExcelMysql.bat запускает проект importExcelMysql.py в домашней директории и считывает файлы с excel.<br>
    Все параметры необходимо подкорректировать в файл config.txt. в проекте должен находиться файл excel. с которого вы импортируете в базу данных.<br>
    - startDropMysqlTables.bat для удаления ненужных таблиц в базе. Скрипт startDropMysqlTables.bat запускает проект dropMysqlTables.py в домашней директории. В файле config.txt нужно заменить параметры БД и названия таблиц через запятую, которые вы ходите удалить.
</p>
<p>
    <strong>Task:</strong><br>
    Необходимо написать скрипт который находит информацию в БД mysql.<br>
    <strong>Decision:</strong><br>
    для работы с проектом использую скрипты bat:<br>
    - startFindTableMysql.bat для поиска таблиц и объектов в БД mysql. Скрипт startFindTableMysql.bat запускает проект findTableMysql.py в домашней директории и запросит действия, которые необходимо сделать. Скрипт может показать список всех БД, список всех таблиц, которые находятся в БД и найти объект в выбраной БД. Необходимо в conifg.txt подключения БД &nbsp;строки начиная с DB_ добавить свои параметры.
</p>
<p>
    <strong>Task:</strong><br>
    В проекте Django есть БД sqlte3. Необходимо проверить содержимое БД и добавить контент в БД.<br>
    <strong>Decision:</strong><br>
    для работы с проектом использую скрипты bat:<br>
    - startfindTableSqlite.bat для поиска содержимого в БД Sqlite3. Для просмотра содержимого БД Sql используется скрипт findTableSqlite.py. скрипт покажет список таблиц БД в Sqlite3. Также нужно в файле config.txt в строке начиная FILTER_TABLE добавить таблицу, которую хотите найти. db.sqlite3 должен быть рядом с этим скриптом.<br>
    - startAddTableSqlite.bat для добавления контента в Django, используя скрипт addTableSqlite.py. в файле addTableSqlite.py необходимо добавить свои параметры таблиц.
</p>
<p>
    <strong>Task:</strong><br>
    Есть инструмент Nokia написанный в VBA, который собирает данные по Nokia c Mysql.<br>
    Добавить кнопку "Add 2100" и дописать макрос, который при нажатии на кнопку "Add 2100" дублирует из таблицы второй несущей LTE1800 и корректирует данные с таблицы параметры (Bandwidth, earfcnDL и LNHOIF / IRFIM instance 0).<br>
    <strong>Decision:</strong><br>
    - в файле 4GCell_DataBuild_.xlsm необходимо снять защиту с листа и добавить возможность изменять код<br>
    Код:<br>
    Private Sub CommandButton3_Click()<br>
    &nbsp; &nbsp;'MsgBox ("This is test code")<br>
    &nbsp; &nbsp;Sheets("Main").Unprotect<br>
    &nbsp; &nbsp;Range("A5:U7").Copy _<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Destination:=Range("A26:U28")<br>
    &nbsp; &nbsp;Sheets("Main").Protect<br>
    &nbsp; &nbsp;For Each cc In [I26:I28]<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Unprotect<br>
    &nbsp; &nbsp; &nbsp; &nbsp;If cc.Value = "15" Then cc.Offset(, 0) = "10"<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Protect<br>
    &nbsp; &nbsp;Next<br>
    &nbsp; &nbsp;For Each cc In [K26:K28]<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Unprotect<br>
    &nbsp; &nbsp; &nbsp; &nbsp;If cc.Value = "1875" Then cc.Offset(, 0) = "100"<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Protect<br>
    &nbsp; &nbsp;Next<br>
    &nbsp; &nbsp;For Each cc In [P26:P28]<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Unprotect<br>
    &nbsp; &nbsp; &nbsp; &nbsp;If cc.Value = "100" Then cc.Offset(, 0) = "1875"<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Protect<br>
    &nbsp; &nbsp;Next<br>
    &nbsp; &nbsp;For Each cc In [J26:J28]<br>
    &nbsp; &nbsp; &nbsp; &nbsp;lte2100 = cc + 40<br>
    &nbsp; &nbsp; &nbsp; 'MsgBox (lte2100)<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Unprotect<br>
    &nbsp; &nbsp; &nbsp; &nbsp;If cc.Value = cc Then cc.Offset(, 0) = lte2100<br>
    &nbsp; &nbsp; &nbsp; &nbsp;Sheets("Main").Protect<br>
    &nbsp; &nbsp;Next<br>
    &nbsp; &nbsp;'Sheets("Main").Protect<br>
    End Sub
</p>
<p>
    <strong>Task:</strong><br>
    Написать проект, который делает выполняет подключение к БД MySql и выгружает &nbsp;таблицу из Mysql<br>
    <strong>Decision:</strong><br>
    Проект работает в файле findInfo.xlsm<br>
    для настройки проекта:<br>
    - Visual Basic - Tools - References - +Microsoft ActiveX Data Objects 6.1 Library - ok<br>
    для запуска в файле findInfo.xlsm необходимо поменять параметры БД и режиме разработчика менять запросы.<br>
    Код:<br>
    Private Sub ConnectionDB()<br>
    &nbsp; &nbsp;Dim oConn As Object<br>
    &nbsp; &nbsp;Set oConn = New ADODB.Connection &nbsp; <br>
    &nbsp; &nbsp;oConn.Open "DRIVER={MySQL ODBC 8.0 Unicode Driver};Server=tipwindows;Database=tbase;User=tuser;Password=tpassword;PORT:3306;Option=3"<br>
    &nbsp; &nbsp;If oConn.State = adStateOpen Then<br>
    &nbsp; &nbsp; &nbsp; &nbsp;MsgBox "Connected! =)"<br>
    &nbsp; &nbsp;End If<br>
    &nbsp; &nbsp;Dim cmd As ADODB.Command &nbsp;'переменная в которой будет запрос<br>
    &nbsp; &nbsp;Set cmd = New ADODB.Command &nbsp; <br>
    &nbsp; &nbsp;Dim rec As ADODB.Recordset 'переменная в которой будет результат запроса<br>
    &nbsp; &nbsp;Set rec = New ADODB.Recordset &nbsp; <br>
    &nbsp; &nbsp;Set cmd.ActiveConnection = oConn<br>
    &nbsp; &nbsp;cmd.CommandText = "SELECT * FROM bss_2g_nokia" 'собственно, запрос<br>
    &nbsp; &nbsp;cmd.CommandType = adCmdText<br>
    &nbsp; &nbsp;cmd.Execute &nbsp; <br>
    &nbsp; &nbsp;Set rec.ActiveConnection = oConn<br>
    &nbsp; &nbsp;rec.Open cmd &nbsp; <br>
    &nbsp; &nbsp;oConn.Close <br>
    End Sub<br>
    - для запуска в файле findInfo.xlsm необходимо поменять параметры БД и в режиме разработчика менять запросы заменив строку SQLStr на запрос, который необоходимо выполнить<br>
    в Лист1 -отобразится информация после запуска кода.
</p>
<p>
    <strong>Task:</strong><br>
    В проекте 4GCell_DataBuild_.xlsm Не загружает таблицу из БД с таким запросом:<br>
    SELECT b.cellName as NSector<br>
    &nbsp; &nbsp; &nbsp;,SUBSTRING(CAST(b.cellName as CHAR),1,6) as SiteName<br>
    &nbsp; &nbsp; &nbsp;,bt.enbName as SystemModule<br>
    &nbsp; &nbsp; &nbsp;, ROUND(POWER(10, e.pMAX/100)/1000,0) as Pmax &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>
    &nbsp; &nbsp; &nbsp;,CAST((CAST(CAST(l.ulChBw AS CHAR) AS INT)/10) AS INT) AS Bandwidth &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<br>
    &nbsp; &nbsp; &nbsp;,l.LNCEL as CID &nbsp; &nbsp; &nbsp;<br>
    &nbsp; &nbsp; &nbsp;,l.earfcnDL<br>
    &nbsp; &nbsp; &nbsp;,e.phyCellId AS PCI &nbsp; &nbsp;<br>
    &nbsp; &nbsp; &nbsp;,l.rootSeqIndex &nbsp; &nbsp; <br>
    &nbsp; &nbsp; &nbsp;,(CASE WHEN CAST(l.prachCS as CHAR) = '14' THEN '35(область)' ELSE '15(город)' END) AS CellRange<br>
    &nbsp; &nbsp; &nbsp;,e.tac as TAC <br>
    &nbsp; &nbsp; &nbsp;,(CASE WHEN l.dlMimoMode = 0 THEN 'SingleTx' ELSE '' END) as SingleTx&nbsp;&nbsp;&nbsp;&nbsp; <br>
    FROM YOURDB1.LNCEL_begin b<br>
    &nbsp;LEFT OUTER JOIN<br>
    &nbsp;(SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    &nbsp; UNION<br>
    &nbsp; SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) l ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    &nbsp;LEFT OUTER JOIN YOURDB1.LNCEL_end e ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL <br>
    &nbsp;LEFT OUTER JOIN YOURDB1.LNBTS_begin bt ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS<br>
    WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')<br>
    ORDER BY b.MRBTS, b.LNCEL<br>
    <strong>Decision:</strong><br>
    Перед запуском необходимо проверить настройки листа:<br>
    - Excel - Рецензирование - Снять защиту с листа - пробовать обновить лист тем же запросом - за 25 минут загрузил и 26845 строк стало в таблице LIST - в LIST отобразились недостающие довесы<br>
    Алгортим:<br>
    - два вложенных запроса, проверьте сначала их по отдельности:<br>
    SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD<br>
    - UNION Проверьте:<br>
    SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD<br>
    - Составьте таблицу, которая получится после выполнения всех JOIN (можно проверять не все сразу, а добавлять по одному):<br>
    SELECT * FROM YOURDB1.LNCEL_begin AS b<br>
    - Запрос не выдал результат. командой show tables определил что изменилось название таблицы:<br>
    SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b<br>
    - следующий запрос:<br>
    SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b<br>
    LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l<br>
    ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    - следующий запрос:<br>
    SELECT * FROM YOURDB1.LNCEL_end AS e<br>
    - Запрос не выдал результат. командой show tables определил что изменилось название таблицы:<br>
    SELECT * FROM YOURDB1_LNCEL.LNCEL_end AS e<br>
    - следующий запрос:<br>
    SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b<br>
    LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l<br>
    ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    LEFT OUTER JOIN YOURDB1.LNCEL_end AS e<br>
    ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL<br>
    - следующий запрос:<br>
    SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b<br>
    LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l<br>
    ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e<br>
    ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL<br>
    - следующий запрос:<br>
    SELECT * FROM YOURDB1.LNBTS_begin AS bt<br>
    - следующий запрос:<br>
    SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b<br>
    LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l<br>
    ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e<br>
    ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL<br>
    LEFT OUTER JOIN YOURDB1.LNBTS_begin AS bt<br>
    ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS<br>
    - Посмотрите, есть ли в выводе поле b.cellName, соответствует ли оно вашему фильтру Where. Примените фильтр к запросу:<br>
    SELECT * FROM YOURDB1_LNCEL.LNCEL_begin AS b<br>
    LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l<br>
    ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e<br>
    ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL<br>
    LEFT OUTER JOIN YOURDB1.LNBTS_begin AS bt<br>
    ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS<br>
    WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')<br>
    ORDER BY b.MRBTS, b.LNCEL<br>
    - Уберите звёздочку, добавляйте по одному полю в выражение SELECT:<br>
    SELECT<br>
    &nbsp; &nbsp;l.LNCEL AS CID,<br>
    &nbsp; &nbsp;l.earfcnDL, l.rootSeqIndex,<br>
    &nbsp; &nbsp;CAST((CAST(CAST(l.ulChBw AS CHAR) AS INT)/10) AS INT) AS Bandwidth,<br>
    &nbsp; &nbsp;(CASE WHEN CAST(l.prachCS as CHAR) = '14' THEN '35(область)' ELSE '15(город)' END) AS CellRange,<br>
    &nbsp; &nbsp;(CASE WHEN l.dlMimoMode = 0 THEN 'SingleTx' ELSE '' END) AS SingleTx,<br>
    &nbsp; &nbsp;b.cellName AS NSector,<br>
    &nbsp; &nbsp;SUBSTRING(CAST(b.cellName as CHAR),1,6) AS SiteName,<br>
    &nbsp; &nbsp;e.phyCellId AS PCI,<br>
    &nbsp; &nbsp;e.tac,<br>
    &nbsp; &nbsp;ROUND(POWER(10, e.pMAX/100)/1000,0) AS Pmax,<br>
    &nbsp; &nbsp;bt.enbName AS SystemModule<br>
    FROM YOURDB1_LNCEL.LNCEL_begin AS b<br>
    LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l<br>
    ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    LEFT OUTER JOIN YOURDB1_LNCEL.LNCEL_end AS e<br>
    ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL<br>
    LEFT OUTER JOIN YOURDB1.LNBTS_begin AS bt<br>
    ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS<br>
    WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')<br>
    ORDER BY b.MRBTS, b.LNCEL<br>
    - Общий результат по проверке запроса:<br>
    +SELECT<br>
    +l.LNCEL,<br>
    +l.earfcnDL,<br>
    +l.rootSeqIndex,<br>
    +CAST((CAST(CAST(l.ulChBw AS CHAR) AS INT)/10) AS INT),<br>
    +(CASE WHEN CAST(l.prachCS as CHAR) = '14' THEN '35(область)' ELSE '15(город)' END),<br>
    +(CASE WHEN l.dlMimoMode = 0 THEN 'SingleTx' ELSE '' END),<br>
    +b.cellName,<br>
    +SUBSTRING(CAST(b.cellName as CHAR),1,6),<br>
    +e.phyCellId,<br>
    +e.tac,<br>
    +ROUND(POWER(10, e.pMAX/100)/1000,0),<br>
    +bt.enbName<br>
    -FROM YOURDB1.LNCEL_begin AS b<br>
    +LEFT OUTER JOIN (SELECT NetActNo, MRBTS, LNBTS, LNCEL, ulChBw, earfcnDL, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_FDD<br>
    +UNION SELECT NetActNo, MRBTS, LNBTS, LNCEL, ChBw, earfcn, rootSeqIndex, prachCS, dlMimoMode FROM YOURDB1.LNCEL_TDD) AS l<br>
    +ON b.NetActNo = l.NetActNo AND b.MRBTS = l.MRBTS AND b.LNBTS = l.LNBTS AND b.LNCEL = l.LNCEL<br>
    -LEFT OUTER JOIN YOURDB1.LNCEL_end AS e<br>
    +ON b.MRBTS = e.MRBTS AND b.LNBTS = e.LNBTS AND b.LNCEL = e.LNCEL<br>
    +LEFT OUTER JOIN YOURDB1.LNBTS_begin bt<br>
    +ON b.NetActNo = bt.NetActNo AND b.MRBTS = bt.MRBTS AND b.LNBTS = bt.LNBTS<br>
    +WHERE SUBSTRING(CAST(b.cellName as CHAR),1,2) IN ('IR','KM','MD','SA','AN','BI','HB','IO')<br>
    +ORDER BY b.MRBTS, b.LNCEL<br>
    - Убрал order BY для быстрого выполнения запроса
</p>
<p>
    <strong>Task:</strong><br>
    Написать скрипт в Python, который выполняет запросы с mysql<br>
    <strong>Decision:</strong><br>
    для работы с проектом использую скрипты bat:<br>
    - startSelectMysql.bat для запуска проекта selectMysql.py. в Файле config.txt нужно заменить параметеры БД и FILTER_TABLE
</p>
<p>
    <strong>Task:</strong><br>
    Разработка ETL процесса, получающий ежедневную выгрузку данных (предоставляется за 3 дня), загружающий ее в хранилище данных и ежедневно строящий отчет.<br>
    Ежедневно некие информационные системы выгружают три следующих файла:<br>
    1. Список транзакций за текущий день. Формат – CSV.<br>
    2. Список терминалов полным срезом. Формат – XLSX.<br>
    3. Список паспортов, включенных в «черный список» - с накоплением с начала месяца. Формат – XLSX.<br>
    Сведения о картах, счетах и клиентах хранятся в СУБД PostgreSQL. Во вложении реквизиты для подключения.<br>
    Вам предоставляется выгрузка за последние три дня, ее надо обработать. В качестве хранилища выступает ваша учебная база (edu). Данные должны быть загружены в хранилище со следующей структурой (имена сущностей указаны по существу, без особенностей правил нейминга, указанных далее).<br>
    Типы данных в полях можно изменять на однородные если для этого есть необходимость. Имена полей менять нельзя. Ко всем таблицам SCD1 должны<br>
    быть добавлены технические поля create_dt, update_dt; ко всем таблицам SCD2 должны быть добавлены технические поля effective_from, effective_to, deleted_flg.<br>
    По результатам загрузки ежедневно необходимо строить витрину отчетности по мошенническим операциям. Витрина строится накоплением, каждый новый отчет укладывается в эту же таблицу с новым report_dt.<br>
    В витрине должны содержаться следующие поля:<br>
    1. event_dt - Время наступления события. Если событие наступило по результату нескольких действий – указывается время действия, по которому установлен факт мошенничества.<br>
    2. passport - Номер паспорта клиента, совершившего мошенническую операцию.<br>
    3. fio - ФИО клиента, совершившего мошенническую операцию.<br>
    4. phone - Номер телефона клиента, совершившего мошенническую операцию.<br>
    5. event_type - Описание типа мошенничества.<br>
    6. report_dt - Время построения отчета.<br>
    Признаки мошеннических операций:<br>
    1. Совершение операции при просроченном или заблокированном паспорте.<br>
    2. Совершение операции при недействующем договоре.<br>
    3. Совершение операций в разных городах в течение одного часа.<br>
    4. Попытка подбора суммы. В течение 20 минут проходит более 3х операций соследующим шаблоном – каждая последующая меньше предыдущей, при этом отклонены все кроме последней. Последняя операция (успешная) в такой цепочке считается мошеннической.<br>
    При именовании таблиц необходимо придерживаться следующих правил (для автоматизации проверки):<br>
    1. tuser.&lt;CODE&gt;_STG_&lt;TABLE_NAME&gt; - Таблицы для размещения стейджинговых таблиц (первоначальная загрузка), промежуточное выделение инкремента, если требуется. Временные таблицы, если такие потребуются в расчете, можно также складывать с таким именованием. Имя таблиц можете выбирать произвольное, но смысловое.<br>
    2. tuser.&lt;CODE&gt;_DWH_FACT_&lt;TABLE_NAME&gt; - Таблицы фактов, загруженных в хранилище. В качестве фактов выступают сами транзакции и «черный список» паспортов. Имя таблиц – как в ER диаграмме.<br>
    3. tuser.&lt;CODE&gt;_DWH_DIM_&lt;TABLE_NAME&gt; - Таблицы измерений, хранящиеся в формате SCD1. Имя таблиц – как в ER диаграмме.<br>
    4. tuser.&lt;CODE&gt;_DWH_DIM_&lt;TABLE_NAME&gt;_HIST - Таблицы измерений, хранящиеся в SCD2 формате (только для тех, кто выполняет усложненное задание). Имя таблиц – как в ER диаграмме.<br>
    5. tuser.&lt;CODE&gt;_REP_FRAUD - Таблица с отчетом.<br>
    6. tuser.&lt;CODE&gt;_META_&lt;TABLE_NAME&gt; - Таблицы для хранения метаданных. Имя таблиц можете выбирать произвольное, но смысловое.<br>
    7. &lt;CODE&gt; - 4 буквы вашего персонального кода.<br>
    Выгружаемые файлы именуются согласно следующему шаблону:<br>
    1. transactions_DDMMYYYY.txt<br>
    2. passport_blacklist_DDMMYYYY.xlsx<br>
    3. terminals_DDMMYYYY.xlsx<br>
    Предполагается что в один день приходит по одному такому файлу. После загрузки соответствующего файла он должен быть переименован в файл с расширением .backup чтобы при следующем запуске файл не искался и перемещен в каталог archive:<br>
    1. transactions_DDMMYYYY.txt.backup<br>
    2. passport_blacklist_DDMMYYYY.xlsx.back<br>
    3. upterminals_DDMMYYYY.xlsx.backup<br>
    Желающие могут придумать, обосновать и реализовать более технологичные и учитывающие сбои способы обработки (за это будет повышен балл).<br>
    В classroom выкладывается zip-архив, содержащий следующие файлы и каталоги:<br>
    1. main.py - Файл, обязательный. Основной процесс обработки.<br>
    2. файлы с данными - Файл, обязательный. Те файлы, которые вы получили в качестве задания. Просто скопируйте все 9 файлов.<br>
    3. main.ddl - Файл, обязательный. Файл с SQL кодом для создания всех необходимых объектов в базе edu.<br>
    4. main.cron - Файл, обязательный. Файл для постановки вашего процесса на расписание, в формате crontab<br>
    5. archive - Каталог, обязательный. Пустой, сюда должны перемещаться отработанные файлы<br>
    6. sql_scripts - Каталог, необязательный. Если вы включаете в main.py какие-то SQL скрипты, вынесенные в отдельные файлы – помещайте их сюда.<br>
    7. py_scripts - Каталог, необязательный. Если вы включаете в main.py какие-то python скрипты, вынесенные в отдельные файлы – помещайте их сюда.<br>
    <strong>Decision:</strong><br>
    проект находится в папке Projects (BankDataWarehouse)<br>
    1. Команды для настройки проекта:<br>
    mkdir archive<br>
    touch snippet_pg.py<br>
    chmod +x snippet_pg.py<br>
    touch main.cron<br>
    touch SCD1_incremental_full_script.sql<br>
    wget https://drive.google.com/file/d/13WSK0C1Z36hhsopebgEv2bGLAoxEsLUp/view?usp=drive_web&amp;authuser=0<br>
    unzip data.zip<br>
    2. Команды для настройки python:<br>
    apt install python3.10-venv<br>
    python3.10 -m venv venv<br>
    source venv/bin/activate<br>
    pip install pandas
</p>
<p>
    <strong>Task:</strong><br>
    Создадите таблицы в базе (main.ddl).<br>
    Алгоритм для файла main.py: Подключитесь к двум базам, Очистите весь стейджинг. Загрузите файлы transactions_01032021.txt, terminals_01032021.xlsx, passport_blacklist_01032021.xlsx в стейджинг. Загрузите таблицы clients, accounts, cards в стейджинг. Используйте следующий подход: Выполните запрос к базе 1, Сохраните полученный результат в DataFrame, Загрузите DataFrame в базу 2. Загрузите данные из стейджинга в целевую таблицу xxxx_dwh_dim_terminals, xxxx_dwh_dim_cards, xxxx_dwh_dim_accounts, xxxx_dwh_dim_clients. Загрузите данные из стейджинга в целевую таблицу xxxx_dwh_fact_passport_blacklist, xxxx_dwh_fact_transactions.. Фактовые таблицы данные перекладываются «простым инсертом», то есть необходимо выполнить один INSERT INTO ... SELECT .... Напишите скрипт, соединяющий нужные таблицы для поиска операций, совершенных при недействующем договоре. Отладьте ваш скрипт для одной даты PgAdmin, он должен выдавать результат. Результат выполнения скрипта загружайте в таблицу xxxx_rep_fraud. Незабывайте сформировать поле report_dt. Зафиксируйте изменения. Отключитесь от баз. Переименуйте обработанные файлы и перенесите их в другой каталог. отладить его работоспособность навсех трех днях загрузки.<br>
    Заполните файл main.cron расписанием и командой исполнения вашего скрипта. Расписание установите так, как считаете нужным чтобы ваши данные заполнились корректно.<br>
    <strong>Decision:</strong><br>
    1. Команды для работы с проектом:<br>
    touch main.py<br>
    python3 main.py<br>
    ls archive/<br>
    passport_blacklist_01032021.xlsx.backup terminals_01032021.xlsx.backup transactions_01032021.txt.backup<br>
    psql -U tuser<br>
    select * from tuser.XXXX_rep_fraud;<br>
    2. По следующим признакам получилось выявить мошеннические транзакции: выполнение операции с просроченным или заблокированным паспортом, выполнение операции с недействительным контрактом, выполнение операций в разных городах в течение одного часа
</p>