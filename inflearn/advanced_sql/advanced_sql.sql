--
-- 중략 --
--

(
select a.d_day, a.sum_amount, a.rnum, b.d_day as d_day_back, b.sum_amount as sum_amount_back, b.rnum as rnum_back
from temp_01 a
join temp_01 b on a.rnum between b.rum and b.rum + 4
)
select d_day
    , avg(sum_amount_back) as m_avg_5days
    , sum(sum_amount_back)/5 as m_avg_5days_01
    , sum(case when rnum - rnum_back = 4 then 0.5 * sum_amount_back
            when rnum - rnum_back in (3,2,1) then sum_amount_back 
            when rnum - rnum_back = 0 then 1.5 * sum_amount_back end) as m_weighted_sum
    , sum(case when rnum - rnum_back = 4 then 0.5 * sum_amount_back
            when rnum - rnum_back in (3,2,1) then sum_amount_back 
            when rnum - rnum_back = 0 then 1.5 * sum_amount_back end) / 5 as m_w_avg_sum
    -- 5건이 안 되는 초기 데이터 삭제하기 위해서
    , count(*) as cnt
from temp_02
group by d_day
having count(*) = 5
order by d_day