#!/usr/bin/python3
import pandas as pd
import psycopg2
import os
###################Подключение к базам
#conn_YOUR-DB1 = psycopg2.connect(database = "testdb",host = "127.0.0.1",user = "testuser",password = "TestP@$$w0rd",port = "5432")
conn_YOUR-DB1 = psycopg2.connect(database = "YOUR-DB1",host = "YOUR-HOST",user = "YOUR-USERNAME1",password = "YOUR-PASSWORD1",port = "5432")
conn_bank_src = psycopg2.connect(database = "bank",host = "YOUR-HOST",user = "YOUR-USERNAME2",password = "YOUR-PASSWORD2",port = "5432")
conn_YOUR-DB1.autocommit = False
conn_bank_src.autocommit = False
cursor_YOUR-DB1 = conn_YOUR-DB1.cursor()
cursor_bank_src = conn_bank_src.cursor()
######################################
###################Очистка стейджинговых таблиц
cursor_YOUR-DB1.execute("""DELETE FROM YOUR-USERNAME1.gabn_stg_transactions;""")
###################Загрузка данных в стейджинг
#df = pd.read_csv(f'/home/YOUR-USERNAME1/gabn/project/data/transactions_01032021.txt', sep=';', decimal=',', header=0, index_col=None)
dirpath = "/home/YOUR-USERNAME1/gabn/project"
project_files = os.listdir(dirpath)
for transactions in project_files:
        if transactions.endswith('.txt'):
                df = pd.read_csv(transactions, sep=";")
                datenow_w_txt = transactions.rsplit('_')[1]
                datenow_str = datenow_w_txt.split('.')[0]
df['amount'] = df['amount'].map(lambda z: z.strip().replace(',', '.')).astype('float')
df['create_dt'] = datenow_str
df['update_dt'] = datenow_str
###################
cursor_YOUR-DB1.executemany("""
                INSERT INTO YOUR-USERNAME1.gabn_stg_transactions(trans_id, trans_date, amt, card_num, oper_type, oper_result, terminal , create_dt, update_dt) 
                VALUES(%s, %s , %s , %s , %s , %s , %s, to_timestamp(%s,'DDMMYYYY'), to_timestamp(%s,'DDMMYYYY'))
        """, df.values.tolist())
###################Загрузка данных в целевые таблицы фактов
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_dwh_fact_transactions (trans_id,trans_date,card_num,oper_type,amt,oper_result,terminal,create_dt,update_dt)
                SELECT stg.trans_id,stg.trans_date,stg.card_num,stg.oper_type,stg.amt,stg.oper_result,stg.terminal,stg.create_dt,stg.update_dt 
                FROM YOUR-USERNAME1.gabn_stg_transactions as stg;
        """)
###################
######################################
###################Очистка стейджинговых таблиц
cursor_YOUR-DB1.execute("""DELETE FROM YOUR-USERNAME1.gabn_stg_terminals;""")
###################Загрузка данных в стейджинг
#df = pd.read_excel(f'/home/YOUR-USERNAME1/gabn/project/data/terminals_01032021.xlsx', sheet_name='terminals', header=0, index_col=None)
for terminals in project_files:
        if terminals.startswith('terminals'):
                df = pd.read_excel(terminals, sheet_name='terminals', header=0, index_col=None )
                datenow_w_txt = terminals.rsplit('_')[1]
                datenow_str = datenow_w_txt.split('.')[0]
df['create_dt'] = datenow_str
df['update_dt'] = datenow_str
#df.insert(4, 'update_dt','2021-03-01')
###################
cursor_YOUR-DB1.executemany("""
                INSERT INTO YOUR-USERNAME1.gabn_stg_terminals(terminal_id,terminal_type,terminal_city,terminal_address,create_dt,update_dt)
                VALUES(%s,%s,%s,%s,to_timestamp(%s,'DDMMYYYY'),to_timestamp(%s,'DDMMYYYY'));
        """, df.values.tolist())
###################Загрузка данных в целевые таблицы измерений
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_dwh_dim_terminals (terminal_id,terminal_type,terminal_city,terminal_address,create_dt,update_dt)
                SELECT stg.terminal_id, stg.terminal_type, stg.terminal_city, stg.terminal_address, stg.update_dt,to_timestamp('9999-12-31', 'YYYY-MM-DD') 
                from YOUR-USERNAME1.gabn_stg_terminals as stg  
                left join YOUR-USERNAME1.gabn_dwh_dim_terminals as trg
                on stg.terminal_id = trg.terminal_id 
                where trg.terminal_id is null;
        """)
###################
######################################
###################Очистка стейджинговых таблиц
cursor_YOUR-DB1.execute("""DELETE FROM YOUR-USERNAME1.gabn_stg_blacklist;""")
###################Загрузка данных в стейджинг
#df = pd.read_excel(f'/home/YOUR-USERNAME1/gabn/project/data/passport_blacklist_01032021.xlsx', sheet_name='blacklist', header=0, index_col=None)
for blacklist in project_files:
        if blacklist.startswith('passport_blacklist'):
                df = pd.read_excel(blacklist, sheet_name='blacklist', header=0, index_col=None )
                datenow_w_ext = blacklist.rsplit('blacklist_')[1]
                datenow_str = datenow_w_ext.split('.')[0]
df['create_dt'] = datenow_str
df['update_dt'] = datenow_str
###################
cursor_YOUR-DB1.executemany("""
                INSERT INTO YOUR-USERNAME1.gabn_stg_blacklist(entry_dt,passport_num,create_dt,update_dt)
                VALUES(%s, %s,to_timestamp(%s,'DDMMYYYY'),to_timestamp(%s,'DDMMYYYY'));
        """, df.values.tolist())
###################Загрузка данных в целевые таблицы фактов
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_dwh_fact_passport_blacklist 
                SELECT stg.passport_num,stg.entry_dt,stg.create_dt,stg.update_dt
                from YOUR-USERNAME1.gabn_stg_blacklist as stg 
                left join YOUR-USERNAME1.gabn_dwh_fact_passport_blacklist as trg 
                on stg.passport_num = trg.passport_num 
                where trg.passport_num is null;
        """)
######################################
###################Очистка стейджинговых таблиц
cursor_YOUR-DB1.execute("""DELETE FROM YOUR-USERNAME1.gabn_stg_cards;""")
###################Загрузка данных в стейджинг
cursor_bank_src.execute("""
                --SELECT regexp_replace(card_num, '\s+$', '') as card_num,account,create_dt,update_dt 
                SELECT card_num,account,create_dt,update_dt 
                FROM info.cards
        """)
records = cursor_bank_src.fetchall()
#for row in records:
#    print(row)
names = [ x[0] for x in cursor_bank_src.description ]
df = pd.DataFrame( records, columns = names )
cursor_YOUR-DB1.executemany("""
                INSERT INTO YOUR-USERNAME1.gabn_stg_cards(card_num,account_num,create_dt,update_dt) 
                VALUES(%s,%s,%s,%s)
        """, df.values.tolist())
###################Загрузка данных в целевые таблицы измерений
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_dwh_dim_cards (card_num,account_num,create_dt,update_dt)
                SELECT stg.card_num, stg.account_num, stg.create_dt, to_timestamp('9999-12-31', 'YYYY-MM-DD')
                from YOUR-USERNAME1.gabn_stg_cards as stg 
                left join YOUR-USERNAME1.gabn_dwh_dim_cards as trg 
                on stg.card_num = trg.card_num 
                where trg.card_num is null;
        """)
###################
######################################
###################Очистка стейджинговых таблиц
cursor_YOUR-DB1.execute("""DELETE FROM YOUR-USERNAME1.gabn_stg_accounts;""")
###################Загрузка данных в стейджинг
cursor_bank_src.execute("""
                SELECT account,valid_to,client,create_dt,update_dt 
                FROM info.accounts
        """)
records = cursor_bank_src.fetchall()
#for row in records:
#        print(row)
names = [ x[0] for x in cursor_bank_src.description ]
df = pd.DataFrame( records, columns = names )
cursor_YOUR-DB1.executemany("""
                INSERT INTO YOUR-USERNAME1.gabn_stg_accounts(account_num,valid_to,client,create_dt,update_dt)
                VALUES( %s, %s, %s, %s, %s)
        """, df.values.tolist())
###################Загрузка данных в целевые таблицы измерений
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_dwh_dim_accounts(account_num,valid_to,client,create_dt,update_dt) 
                SELECT stg.account_num,stg.valid_to,stg.client,stg.create_dt,to_timestamp('9999-12-31', 'YYYY-MM-DD')
                        from YOUR-USERNAME1.gabn_stg_accounts as stg 
                left join YOUR-USERNAME1.gabn_dwh_dim_accounts as trg
                on stg.account_num = trg.account_num 
                where trg.account_num is null;
        """)
###################
######################################
###################Очистка стейджинговых таблиц
cursor_YOUR-DB1.execute("""DELETE FROM YOUR-USERNAME1.gabn_stg_clients;""")
###################Загрузка данных в стейджинг
cursor_bank_src.execute("""
                SELECT client_id,last_name,first_name,patronymic,date_of_birth,passport_num,passport_valid_to,phone,create_dt,update_dt
                FROM info.clients; 
        """)
records = cursor_bank_src.fetchall()
#for row in records:
#        print(row)
names = [ x[0] for x in cursor_bank_src.description ]
df = pd.DataFrame(records, columns = names) 
cursor_YOUR-DB1.executemany(""" 
                INSERT INTO YOUR-USERNAME1.gabn_stg_clients(client_id,last_name,first_name,patronymic,date_of_birth,passport_num,passport_valid_to,phone,create_dt,update_dt)
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
        """, df.values.tolist()) 
###################Загрузка данных в целевые таблицы измерений
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_dwh_dim_clients(client_id,last_name,first_name,patronymic,date_of_birth,passport_num,passport_valid_to,phone,create_dt,update_dt)
                SELECT stg.client_id,stg.last_name,stg.first_name,stg.patronymic,stg.date_of_birth,stg.passport_num,stg.passport_valid_to,stg.phone,stg.create_dt,now()
                from YOUR-USERNAME1.gabn_stg_clients as stg
                left join YOUR-USERNAME1.gabn_dwh_dim_clients as trg
                on stg.client_id = trg.client_id 
                where trg.client_id is null;
        """)
###################
######################################
###################Выявление мошеннических операций и построение отчёта
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_rep_fraud 
                select 
                        min(t2.trans_date) as trans_date, 
                        tgddcl.passport_num as passport_num, 
                        (tgddcl.last_name || ' ' || tgddcl.first_name || ' ' || tgddcl.patronymic ) as fio, 
                        tgddcl.phone as phone, 
                        '1' as event_type,
                        now() as report_dt
                from (
                        select *
                        from (
                                with current_dt as ( 
                                        select trans_date 
                                        from YOUR-USERNAME1.gabn_stg_transactions) 
                                select  tgdft.*, tgddca.account_num 
                                from YOUR-USERNAME1.gabn_dwh_fact_transactions as tgdft 
                                left join YOUR-USERNAME1.gabn_dwh_dim_cards as tgddca
                                on trim(tgdft.card_num) = trim(tgddca.card_num ) 
                                where tgdft.oper_result = 'SUCCESS' 
                                        and tgdft.trans_date in (
                                                select trans_date 
                                                from current_dt)) as t 
                        left join YOUR-USERNAME1.gabn_dwh_dim_accounts as gdda 
                        on t.account_num = gdda.account_num ) as t2 
                left join YOUR-USERNAME1.gabn_dwh_dim_clients as tgddcl 
                on t2.client = tgddcl.client_id 
                where (tgddcl.passport_valid_to < t2.trans_date 
                        or tgddcl.passport_num in (
                                select passport_num
                                from YOUR-USERNAME1.gabn_dwh_fact_passport_blacklist))  
                group by tgddcl.passport_num, (tgddcl.last_name || ' ' || tgddcl.first_name || ' ' || tgddcl.patronymic ), tgddcl.phone;
        """)
###################Совершение операции при недействующем договоре.
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_rep_fraud
                select 
                        t2.trans_date as trans_date, 
                        gddcl.passport_num as passport_num, 
                        (gddcl.last_name || ' ' || gddcl.first_name || ' ' || gddcl.patronymic ) as fio, 
                        gddcl.phone as phone, 
                        '2' as event_type,
                        now() as report_dt
                from (
                        select min(t.trans_date) trans_date, t.account_num, gdda.client
                        from (
                                with current_dt as ( 
                                        select trans_date 
                                        from YOUR-USERNAME1.gabn_stg_transactions) 
                                select gdft.trans_date, gdft.card_num, gddca.account_num
                                from YOUR-USERNAME1.gabn_dwh_fact_transactions as gdft 
                                left join YOUR-USERNAME1.gabn_dwh_dim_cards as gddca
                                on trim(gdft.card_num) = trim(gddca.card_num ) 
                                where gdft.oper_result = 'SUCCESS'
                                        and gdft.trans_date in (
                                                select trans_date 
                                                from current_dt)) as t 
                        left join YOUR-USERNAME1.gabn_dwh_dim_accounts as gdda 
                        on t.account_num = gdda.account_num 
                        where t.trans_date > gdda.valid_to
                        group by t.account_num, gdda.client ) as t2 
                left join YOUR-USERNAME1.gabn_dwh_dim_clients as gddcl 
                on t2.client = gddcl.client_id;
        """)
###################Совершение операций в разных городах в течение одного часа
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_rep_fraud
                select
                        t3.trans_date,
                        t3.passport_num,
                        (t3.last_name || ' ' || t3.first_name || ' ' || t3.patronymic ) as fio,
                        t3.phone ,
                        '3' as event_type,
                        now() as report_dt
                from (
                        select trans_date, trg2.*
                        from (
                                select * from (
                                        select * from (
                                                with lds as  (
                                                        select
                                                                trans_date,
                                                                terminal_city,
                                                                card_num,
                                                                lag(terminal_city) over (
                                                                        partition by gdftr.card_num
                                                                        order by gdftr.trans_date) as lag_c,
                                                                lag(trans_date) over (
                                                                        partition by card_num
                                                                        order by gdftr.trans_date) as lag_t,
                                                                lead(terminal_city) over (
                                                                        partition by gdftr.card_num
                                                                        order by gdftr.trans_date) as lead_c ,
                                                                lead(trans_date) over (
                                                                        partition by card_num
                                                                        order by gdftr.trans_date) as lead_t
                                                        from YOUR-USERNAME1.gabn_dwh_fact_transactions as gdftr
                                                        left join YOUR-USERNAME1.gabn_dwh_dim_terminals as gddt
                                                        on gdftr.terminal = gddt.terminal_id
                                                        where gdftr.oper_result = 'SUCCESS'),
                                                current_dt as (
                                                        select trans_date
                                                        from YOUR-USERNAME1.gabn_stg_transactions )
                                                select
                                                        min(trans_date) as trans_date,
                                                        card_num
                                                from lds
                                                where lag_c <> terminal_city
                                                        and (trans_date-lag_t) < '01:00:00'
                                                        and trans_date  in (
                                                                select trans_date
                                                                from current_dt)
                                                group by card_num) as trg
                                        left join YOUR-USERNAME1.gabn_dwh_dim_cards as trg3
                                        on trim(trg.card_num) = trim(trg3.card_num )) as t
                                left join YOUR-USERNAME1.gabn_dwh_dim_accounts as trg4
                                on t.account_num = trg4.account_num ) as t2
                        left join YOUR-USERNAME1.gabn_dwh_dim_clients as trg2
                        on t2.client = trg2.client_id ) as t3;
        """)
###################Попытка подбора суммы
cursor_YOUR-DB1.execute("""
                INSERT INTO YOUR-USERNAME1.gabn_rep_fraud 
                select 
                        t3.trans_date, 
                        t3.passport_num , 
                        (t3.last_name || ' ' || t3.first_name || ' ' || t3.patronymic ) as fio, 
                        t3.phone , 
                        '4' as event_type,
                        now() as report_dt
                from (
                        select 
                                trans_date, 
                                gddcl.*
                        from  (
                                select * from (
                                        select * from(
                                                with rj as (
                                                        select 
                                                                *,
                                                                lag(amt) over (
                                                                        partition by gdft.card_num 
                                                                        order by gdft.trans_date) as lag_a,
                                                                lag(amt,2) over (
                                                                        partition by gdft.card_num 
                                                                        order by gdft.trans_date) as lag_a2,
                                                                lag(amt,3) over (
                                                                        partition by gdft.card_num 
                                                                        order by gdft.trans_date) as lag_a3,
                                                                lag(oper_result) over (
                                                                        partition by gdft.card_num 
                                                                        order by gdft.trans_date) as lag_r,
                                                                lag(oper_result,2) over (
                                                                        partition by gdft.card_num 
                                                                        order by gdft.trans_date) as lag_r2,
                                                                lag(oper_result,3) over (
                                                                        partition by gdft.card_num 
                                                                        order by gdft.trans_date) as lag_r3,
                                                                lag(trans_date,3) over (
                                                                        partition by gdft.card_num 
                                                                        order by gdft.trans_date) as min_t
                                                        from YOUR-USERNAME1.gabn_dwh_fact_transactions gdft),
                                                current_dt as ( 
                                                        select trans_date 
                                                        from YOUR-USERNAME1.gabn_stg_transactions )
                                                select * 
                                                from rj
                                                where oper_result = 'SUCCESS' 
                                                        and lag_r = 'REJECT' 
                                                        and lag_a > amt 
                                                        and lag_r2 = 'REJECT' 
                                                        and lag_a2 > lag_a
                                                        and lag_r3 = 'REJECT' 
                                                        and lag_a3 > lag_a2
                                                        and (trans_date - min_t) <= '00:20:00'
                                                        and trans_date  in (
                                                                select trans_date 
                                                                from current_dt)) as trg
                                        left join YOUR-USERNAME1.gabn_dwh_dim_cards as gddca
                                        on trim(trg.card_num) = trim(gddca.card_num )) as t 
                                left join YOUR-USERNAME1.gabn_dwh_dim_accounts as gdda 
                                on t.account_num = gdda.account_num ) as t2 
                        left join YOUR-USERNAME1.gabn_dwh_dim_clients as gddcl 
                        on t2.client = gddcl.client_id ) as t3;
        """)
######################################
conn_bank_src.commit()
conn_YOUR-DB1.commit()
######################################Запись файлов в архив
os.rename('/home/YOUR-USERNAME1/gabn/project/terminals_01032021.xlsx', '/home/YOUR-USERNAME1/gabn/project/archive/terminals_01032021.xlsx.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/transactions_01032021.txt', '/home/YOUR-USERNAME1/gabn/project/archive/transactions_01032021.txt.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/passport_blacklist_01032021.xlsx', '/home/YOUR-USERNAME1/gabn/project/archive/passport_blacklist_01032021.xlsx.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/terminals_02032021.xlsx', '/home/YOUR-USERNAME1/gabn/project/archive/terminals_02032021.xlsx.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/transactions_02032021.txt', '/home/YOUR-USERNAME1/gabn/project/archive/transactions_02032021.txt.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/passport_blacklist_02032021.xlsx', '/home/YOUR-USERNAME1/gabn/project/archive/passport_blacklist_02032021.xlsx.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/terminals_03032021.xlsx', '/home/YOUR-USERNAME1/gabn/project/archive/terminals_03032021.xlsx.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/transactions_03032021.txt', '/home/YOUR-USERNAME1/gabn/project/archive/transactions_03032021.txt.backup')
os.rename('/home/YOUR-USERNAME1/gabn/project/passport_blacklist_03032021.xlsx', '/home/YOUR-USERNAME1/gabn/project/archive/passport_blacklist_03032021.xlsx.backup')
######################################
cursor_bank_src.close();
cursor_YOUR-DB1.close();
