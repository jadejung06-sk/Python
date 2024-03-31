-- 작년 대비 동월 매출 비교
-- 앞에 있는 데이터(과거 데이터 order by asc)를 가져오는 것 lag
with
temp_01 as (
select date_trunc('month', order_date)::date as month_day
	, sum(amount) as sum_amount
from nw.orders a
	join nw.order_items b on a.order_id = b.order_id
group by date_trunc('month', order_date)::date
),
temp_02 as (
select month_day, sum_amount as curr_amount
	, lag(month_day, 12) over (order by month_day) as prev_month_1year
	, lag(sum_amount, 12) over (order by month_day) as prev_amount_1year
from temp_01
)
select *
	, curr_amount - prev_amount_1year as diff_amount
	, 100.0 * curr_amount / prev_amount_1year as prev_pct
	, 100.0 * (curr_amount - prev_amount_1year) / prev_amount_1year as prev_growth_pct
from temp_02
where prev_amount_1year is not null;

-- 작년 대비 동분기 매출 비교, 작년 동부기 대비 차이/비율/매출 성장 비율 추출
with
temp_01 as (
select date_trunc('quarter', order_date)::date as month_day
	, sum(amount) as sum_amount
from nw.orders a
	join nw.order_items b on a.order_id = b.order_id
group by date_trunc('quarter', order_date)::date
),
temp_02 as (
select month_day, sum_amount as curr_amount
	, lag(month_day, 4) over (order by month_day) as prev_month_1year
	, lag(sum_amount, 4) over (order by month_day) as prev_amount_1year
from temp_01
)
select *
	, curr_amount - prev_amount_1year as diff_amount
	, 100.0 * curr_amount / prev_amount_1year as prev_pct
	, 100.0 * (curr_amount - prev_amount_1year) / prev_amount_1year as prev_growth_pct
from temp_02
where prev_amount_1year is not null;