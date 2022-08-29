select 
    toStartOfMonth(toDate(buy_date)) as month
    , avg(check_amount) as avg_check
    , toFloat32(medianExact(check_amount)) as median_check
    -- , medianExact(check_amount) as median_check
from default.view_checks
group by toStartOfMonth(toDate(buy_date)) 
order by 1 asc;