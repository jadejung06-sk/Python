-- 신규 유저와 기존 유저 분류하여 건수 추출 (세션 건수도 함께 추출)
with temp_01 as (
select a.sess_id, a.user_id, a.visit_stime, b.create_time
	, case when b.create_time between :current_date - interval '30 days' and :current_date then 1
	else 0 end as is_new_user
	from ga.ga_sess a
		join ga.ga_users b on a.user_id = b.user_id	
	where visit_stime >= (:current_date - interval '30 days') and visit_stime < :current_date
)
--select is_new_user, count(*) as cnt
select count(distinct user_id) as user_cnt
	, count(distinct case when is_new_user = 1 then user_id end) as new_usr_cnt
	, count(distinct case when is_new_user = 0 then user_id end) as repeat_usr_cnt
	, count(*) as sess_cnt
from temp_01;
