-- 중간에 기준 표를 넣는 방식에 left join on between 을 통해 만들 수 있음
with temp_01 as (
select a.user_id
, max(date_trunc('day', a.order_time))::date as max_ord_date
, to_date('20161101', 'yyyymmdd') - max(date_trunc('day', a.order_time))::date as recency
, count(distinct a.order_id) as freq
, sum(b.prod_revenue) as money
from orders a 
    join order_items b on a.order_id = b.order_id
group by a.user_id),
temp_02 as (
select 'A' as grade, 1 as fr_rec, 14 as to_rec, 5 as fr_freq, 9999 as to_freq, 300.0 as fr_money, 999999.0 as to_money
union all
select 'B', 15, 50, 3, 4, 50.0, 299.999
union all
select 'C', 51, 99999, 1, 2, 0.0, 49.999
), 
temp_03 as (
select a.*
	, b.grade as recency_grade
	, c.grade as freq_grade
	, d.grade as money_grade
	from temp_01 a
		left join temp_02 b on a.recency between b.fr_rec and b.to_rec
		left join temp_02 c on a.freq between c.fr_freq and c.to_freq
		left join temp_02 d on a.money between d.fr_money and d.to_money 
		-- left를 한 번 쓰면 계속해서 써줘야 빠지는 게 없다
)
select *
	, case when recency_grade = 'A' and freq_grade in ('A', 'B') and money_grade = 'A' then 'A'
		   when recency_grade = 'B' and freq_grade = 'A' and money_grade = 'A' then 'A'
		   when recency_grade = 'B' and freq_grade in ('A', 'B', 'C') and money_grade = 'B' then 'B'
		   when recency_grade = 'C' and freq_grade in ('A', 'B') and money_grade = 'B' then 'B'
		   when recency_grade = 'C' and freq_grade = 'C' and money_grade = 'A' then 'B'
		   when recency_grade = 'C' and freq_grade = 'C' and money_grade in ('B', 'C') then 'C'
		   when recency_grade in ('B', 'C') and money_grade = 'C' then 'C'
		   else 'C' end as total_grade
from temp_03;