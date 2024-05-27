drop table if exists daily_dau;

create table daily_dau
as 
with
temp_00 as (
select generate_series('2016-08-02'::date, '2016-11-01'::date, '1 day'::interval)::date as curr_date
)
select b.curr_date, count(distinct user_id) as dau
from ga.ga_sess a
	cross join temp_00 b
	where visit_stime >= (b.curr_date - interval '1 days') and visit_stime < b.curr_date
	group by b.curr_date;

select * from daily_dau;

drop table if exists daily_wau;

create table daily_wau
as 
with
temp_00 as (
select generate_series('2016-08-02'::date, '2016-11-01'::date, '1 day'::interval)::date as curr_date
)
select b.curr_date, count(distinct user_id) as wau
from ga.ga_sess a
	cross join temp_00 b
	where visit_stime >= (b.curr_date - interval '7 days') and visit_stime < b.curr_date
	group by b.curr_date;


drop table if exists daily_mau;

create table daily_mau
as 
with
temp_00 as (
select generate_series('2016-08-02'::date, '2016-11-01'::date, '1 day'::interval)::date as curr_date
)
select b.curr_date, count(distinct user_id) as mau
from ga.ga_sess a
	cross join temp_00 b
	where visit_stime >= (b.curr_date - interval '30 days') and visit_stime < b.curr_date
	group by b.curr_date;


select * from daily_wau;

alter table daily_wau rename column dau to wau;


create table daily_acquisitions
as
select a.curr_date, a.dau, b.wau, c.mau
from daily_dau a
join daily_wau b on a.curr_date = b.curr_date
join daily_mau c on a.curr_date = c.curr_date;

select * from daily_acquisitions;