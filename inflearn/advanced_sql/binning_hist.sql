-- 주문 분석
-- 주문 테이블에서 이전 주문 이후 걸린 기간 구하기
-- bin 구하기 (10 간격 설정)
with
temp_01 as (
select order_id, customer_id, order_date
	, lag(order_date) over (partition by customer_id order by order_date) as prev_ord_date
from nw.orders
), 
temp_02 as (
select order_id, customer_id, order_date
	, order_date - prev_ord_date as days_since_prev_order
	from temp_01
	where prev_ord_date is not null
)
select floor(days_since_prev_order/10.0)*10 as bin, count(*) bin_cnt
from temp_02 group by floor(days_since_prev_order/10.0)*10 order by 1; 