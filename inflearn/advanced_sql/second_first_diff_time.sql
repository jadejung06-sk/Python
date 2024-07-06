-- 사용자가 첫 세션 접속 후 두번째 세션 접속까지 걸리는 평균, 최대, 최소, 4분위 percentitile 시간 추출
-- postgresql avg(time) 은 interval이 제대로 고려되지 않음. justify_interval()을 적용해야함 : 그렇지 않으면, 24시간 이상의 시간이 뜸
with temp_01 as (
select user_id, visit_stime, row_number() over (partition by user_id order by visit_stime) as sess_rnum
	, count(*) over (partition by user_id) as session_cnt
from ga_sess
order by user_id, sess_rnum),
temp_02 as (
select user_id
, max(visit_stime) as max_time, min(visit_stime) as min_time
, max(visit_stime) - min(visit_stime) as sess_time_diff
from temp_01
where sess_rnum <= 2 and session_cnt > 1
group by user_id)
select justify_interval(avg(sess_time_diff)) as avg_time
	, max(sess_time_diff) as max_time, min(sess_time_diff) as min_time
	, percentile_disc(0.25) within group (order by sess_time_diff) as percentile_1
	, percentile_disc(0.5) within group (order by sess_time_diff) as percentitle_2
	, percentile_disc(0.75) within group (order by sess_time_diff) as percentitle_3
	, percentile_disc(1.0) within group (order by sess_time_diff) as percentitle_4
from temp_02
where sess_time_diff::interval > interval '0 second';
