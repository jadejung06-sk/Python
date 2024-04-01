-- 카테고리별 기준 월 대비 매출 비율 추이 SQL (aka 매출 팬 차트)
-- Step 1 : 상품 카테고리 별 월별 매출액 추출
-- Step 2 : Step 1의 집합에서 기준 월이 되는 첫월의 매출액을 동일 카테고리에 모두 복제한 뒤 매출 비율 계산 
-- sum과 where절은 같이 사용하면 안 됨. where절이 먼저 수행되서 제대로 동작하지 않음 -> temp_01에서 sum을 수행한 후, temp_02에서 where 절 넣기
with 
temp_01 as (
	select to_char(a.order_date, 'yyyymm') as year_month
		, sum(b.amount) as sum_amount
	from nw.orders a
		join nw.order_items b
			on a.order_id = b.order_id
	group by to_char(a.order_date, 'yyyymm')
), 
temp_02 as (
select year_month, substring(year_month, 1, 4) as year
	, sum_amount
	, sum(sum_amount) over (partition by substring(year_month, 1, 4) order by year_month) as acc_amount
	, sum(sum_amount) over (order by year_month rows between 11 preceding and current row) as year_ma_amount
from temp_01 -- where year_month between '199708' and '199805' 와 같이 사용하면 안됨. where절이 먼저 수행되므로 sum() analytics가 제대로 동작하지 않음.
)
select * from temp_02 where year='1997' --where year_month >= '199801' and year_month <= '199805';