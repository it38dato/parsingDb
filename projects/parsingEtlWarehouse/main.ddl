#!/usr/bin/python3
----------------------------------
create table de13ma.gabn_stg_transactions(
    trans_id varchar(15),
    trans_date timestamp(0),
    --amt decimal(10,2),
    amt numeric(10,2),    
    card_num varchar(20),
    oper_type varchar(10),
    oper_result varchar(10),
    terminal varchar(10),
    create_dt timestamp(0), 
    update_dt timestamp(0));
create table de13ma.gabn_dwh_fact_transactions(
    trans_id varchar(15),
    trans_date timestamp(0),
    --amt numeric(10,2),
    amt decimal(10,2),
    card_num varchar(20),
    oper_type varchar(10),
    oper_result varchar(10),
    terminal varchar(10),
    create_dt timestamp(0), 
    update_dt timestamp(0));
----------------------------------
create table de13ma.gabn_stg_terminals(
    terminal_id varchar(10),
    terminal_type varchar(10),
    terminal_city varchar(30),
    terminal_address varchar(70),
    create_dt timestamp(0), 
    update_dt timestamp(0));
create table de13ma.gabn_dwh_dim_terminals(
    terminal_id varchar(10),
    terminal_type varchar(10),
    terminal_city varchar(30),
    terminal_address varchar(70),
    create_dt timestamp(0),
    update_dt timestamp(0),
    effective_from timestamp(0),
    effective_to timestamp(0),
    deleted_flg char(1));
create table de13ma.gabn_stg_del_terminals(
    terminal_id varchar(10));
----------------------------------
create table de13ma.gabn_stg_blacklist(
    passport_num varchar(15),
    --entry_dt date
    entry_dt timestamp(0),
    create_dt timestamp(0), 
    update_dt timestamp(0));
create table de13ma.gabn_dwh_fact_passport_blacklist(
    passport_num varchar(30),
    --entry_dt date
    --date timestamp(0)
    entry_dt timestamp(0),
    create_dt timestamp(0), 
    update_dt timestamp(0));
----------------------------------
create table de13ma.gabn_stg_cards(
    card_num varchar(20),
    account_num varchar(20),
    create_dt timestamp(0),
    update_dt timestamp(0));
create table de13ma.gabn_dwh_dim_cards(
    card_num varchar(20),
    account_num varchar(20),
    --create_dt date,
    --update_dt date
    create_dt timestamp(0), 
    update_dt timestamp(0),
    effective_from timestamp(0),
    effective_to timestamp(0),
    deleted_flg char(1));
create table de13ma.gabn_stg_del_cards(
    card_num varchar(20));
----------------------------------
create table de13ma.gabn_stg_accounts(
    account_num varchar(20),
    --valid_to date,
    valid_to timestamp(0), 
    client varchar(10),
    create_dt timestamp(0),
    update_dt timestamp(0));
create table de13ma.gabn_dwh_dim_accounts(
    account_num varchar(20),
    --valid_to date,
    valid_to timestamp(0), 
    client varchar(10),
    --create_dt date,
    --update_dt date
    create_dt timestamp(0), 
    update_dt timestamp(0),
    effective_from timestamp(0),
    effective_to timestamp(0),
    deleted_flg char(1)); 
create table de13ma.gabn_stg_del_accounts(
    account_num varchar(20));
----------------------------------
create table de13ma.gabn_stg_clients(
    client_id varchar(10),
    last_name varchar(20),
    first_name varchar(20),
    patronymic varchar(20),
    --date_of_birth date,
    date_of_birth timestamp(0), 
    passport_num varchar(15),
    --passport_valid_to date,
    passport_valid_to timestamp(0),
    phone varchar(16),
    create_dt timestamp(0),
    update_dt timestamp(0));
create table de13ma.gabn_dwh_dim_clients(
    client_id varchar(10),
    last_name varchar(20),
    first_name varchar(20),
    patronymic varchar(20),
    --date_of_birth date,
    date_of_birth timestamp(0),
    passport_num varchar(15),
    --passport_valid_to date,
    passport_valid_to timestamp(0),
    phone varchar(16),
    --create_dt date,
    --update_dt date
    create_dt timestamp(0), 
    update_dt timestamp(0),
    effective_from timestamp(0),
    effective_to timestamp(0),
    deleted_flg char(1));
create table de13ma.gabn_stg_del_clients(
    client_id varchar(10));
----------------------------------
create table de13ma.gabn_rep_fraud(
    event_dt timestamp(0), 
    passport varchar(20), 
    fio varchar(50),
    phone varchar(16), 
    event_type varchar(120), 
    --report_dt date
    report_dt timestamp(0));
----------------------------------
create table de13ma.gabn_meta(
    schema_name varchar(30),
    table_name varchar(30),
    max_update_dt timestamp(0));
----------------------------------
