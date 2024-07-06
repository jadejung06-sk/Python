-- 사용자 월별 세션접속 횟수, (월말 3일 이전 생성된 사용자 제외)
-- 주의 : postgresql은 last_day() 월의 마지막 일을 보여주는 함수가 없음
-- 때문에 해당 일자가 속한 달의 첫번째 날짜 가령 10월 5일이면, 10월 1일에 1달을 더하고 거기에 1일을 뺌
-- 10월 5일 -> 10월 1일 구하기 -> 한달을 더 하기 11월 1일 -> 여기에서 하루를 빼서 10월 31일을 출력하는 방법을 써야 함
select user_id, create_time, (date_trunc('month', create_time) + interval '1 month' - interval '1 day')::date
from ga.ga_users
where create_time <= (date_trunc('month', create_time) + interval '1 month' - interval '1 day')::date - 2;
