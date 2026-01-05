drop table de13ma.gabn_stg_transactions;
drop table de13ma.gabn_dwh_fact_transactions;
drop table de13ma.gabn_stg_terminals;
drop table de13ma.gabn_dwh_dim_terminals;
drop table de13ma.gabn_stg_del_terminals;
drop table de13ma.gabn_stg_blacklist;
drop table de13ma.gabn_dwh_fact_passport_blacklist;
drop table de13ma.gabn_stg_cards;
drop table de13ma.gabn_dwh_dim_cards;
drop table de13ma.gabn_stg_del_cards;
drop table de13ma.gabn_stg_accounts;
drop table de13ma.gabn_dwh_dim_accounts;
drop table de13ma.gabn_stg_del_accounts;
drop table de13ma.gabn_stg_clients;
drop table de13ma.gabn_dwh_dim_clients;
drop table de13ma.gabn_stg_del_clients;
drop table de13ma.gabn_rep_fraud;
drop table de13ma.gabn_meta;


select * from de13ma.gabn_stg_transactions;
select * from de13ma.gabn_dwh_fact_transactions;
select * from de13ma.gabn_stg_terminals;
select * from de13ma.gabn_dwh_dim_terminals;
select * from de13ma.gabn_stg_blacklist;
select * from de13ma.gabn_dwh_fact_passport_blacklist;
select * from de13ma.gabn_stg_cards
select * from de13ma.gabn_dwh_dim_cards
select * from de13ma.gabn_stg_clients
select * from de13ma.gabn_dwh_dim_clients

delete from de13ma.gabn_dwh_fact_transactions;
delete from de13ma.gabn_dwh_dim_terminals;
delete from de13ma.gabn_dwh_fact_passport_blacklist;
delete from de13ma.gabn_dwh_dim_cards;
delete from de13ma.gabn_dwh_dim_clients