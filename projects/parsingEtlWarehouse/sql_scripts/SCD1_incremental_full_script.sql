----------------------------------------------------------------------------
-- Подготока данных

create table tuser.XXXX_source(
    id integer,
    val varchar(50),
    update_dt timestamp(0)
);
insert into tuser.XXXX_source ( id, val, update_dt ) values ( 1, 'A', now() );
insert into tuser.XXXX_source ( id, val, update_dt ) values ( 2, 'B', now() );
insert into tuser.XXXX_source ( id, val, update_dt ) values ( 3, 'C', now() );
update tuser.XXXX_source set val = 'X', update_dt = now() where id = 3;
delete from tuser.XXXX_source where id = 3;
create table tuser.XXXX_stg(
    id integer,
    val varchar(50),
    update_dt timestamp(0)
);
create table tuser.XXXX_target (
    id integer,
    val varchar(50),
    create_dt timestamp(0),
    update_dt timestamp(0)
);
create table tuser.XXXX_meta(
  schema_name varchar(30),
  table_name varchar(30),
  max_update_dt timestamp(0)
);
insert into tuser.XXXX_meta( schema_name, table_name, max_update_dt )
values( 'tuser','XXXX_SOURCE', to_timestamp('1900-01-01','YYYY-MM-DD') );
create table tuser.XXXX_stg_del(
    id integer
);
----------------------------------------------------------------------------
-- Инкрементальная загрузка
-- 1. Очистка стейджинговых таблиц
delete from tuser.XXXX_stg;
delete from tuser.XXXX_stg_del;
-- 2. Захват данных из источника (измененных с момента последней загрузки) в стейджинг
insert into tuser.XXXX_stg( id, val, update_dt )
select id, val, update_dt from tuser.XXXX_source
where update_dt > ( select max_update_dt from tuser.XXXX_meta where schema_name='tuser' and table_name='XXXX_SOURCE' );
-- 3. Захват в стейджинг ключей из источника полным срезом для вычисления удалений.
insert into tuser.XXXX_stg_del( id )
select id from tuser.XXXX_source;
-- 4. Загрузка в приемник "вставок" на источнике (формат SCD1).
insert into tuser.XXXX_target( id, val, create_dt, update_dt )
select
    stg.id,
    stg.val,
    stg.update_dt,
    null
from tuser.XXXX_stg stg
left join tuser.XXXX_target trg
on stg.id = trg.id
where trg.id is null;
-- 5. Обновление в приемнике "обновлений" на источнике (формат SCD1).
update tuser.XXXX_target
set
    val = tmp.val,
    update_dt = tmp.update_dt
from (
    select
        stg.id,
        stg.val,
        stg.update_dt,
        null
    from tuser.XXXX_stg stg
        inner join tuser.XXXX_target trg on stg.id = trg.id
    where stg.val <> trg.val
        or ( stg.val is null and trg.val is not null ) or ( stg.val is not null and trg.val is null )
) tmp
where XXXX_target.id = tmp.id;
-- 6. Удаление в приемнике удаленных в источнике записей (формат SCD1).
delete from tuser.XXXX_target
where id in (
    select trg.id
    from tuser.XXXX_target trg
    left join tuser.XXXX_stg_del stg
    on stg.id = trg.id
    where stg.id is null
);
-- 7. Обновление метаданных.
update tuser.XXXX_meta
set max_update_dt = coalesce( (select max( update_dt ) from tuser.XXXX_stg ), ( select max_update_dt from tuser.XXXX_meta where schema_name='tuser' and table_name='XXXX_SOURCE' ) )
where schema_name='tuser' and table_name = 'XXXX_SOURCE';
-- 8. Фиксация транзакции.
commit;