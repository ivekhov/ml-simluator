-- select 
--     toStartOfDay(toDate(timestamp)) as day
--     , toFloat32(count(distinct user_id)) as dau
-- from churn_submits
-- group by toStartOfDay(toDate(timestamp)) 
-- order by toFloat32(toStartOfDay(toDate(timestamp)))

select 
    toDate(timestamp) as day
    , count(distinct user_id) as dau
from churn_submits
group by toDate(timestamp)
order by toDate(timestamp)
