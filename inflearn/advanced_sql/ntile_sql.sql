with temp_01 as (
select a.user_id
, max(date_trunc('day', a.order_time))::date as max_ord_date
, to_date('20161101', 'yyyymmdd') - max(date_trunc('day', a.order_time))::date as recency
, count(distinct a.order_id) as freq
, sum(b.prod_revenue) as money
from orders a 
    join order_items b on a.order_id = b.order_id
group by a.user_id
)
select *
-- 1등급이 가장 높고, 5등급이 가장 낮은 형태
-- freq 는 1이 2273개, 2 199개, 3 50개로 1에 몰려 있는 문제가 있음
-- money 210~1035 까지 rank 1이라는 문제가 있음
	, ntile(5) over (order by recency asc rows between unbounded preceding and unbounded following) as recency_rank
	, ntile(5) over (order by freq desc rows between unbounded preceding and unbounded following) as freq_rank	
	, ntile(5) over (order by money desc rows between unbounded preceding and unbounded following) as money_rank	
from temp_01;