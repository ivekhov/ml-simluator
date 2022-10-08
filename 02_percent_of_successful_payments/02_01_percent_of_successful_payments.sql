SELECT 
    TO_DATE(TO_CHAR(date, 'MM/YY'),  'MM/YY') AS time
    , mode
    , COUNT(
        CASE 
            WHEN status = 'Confirmed' THEN 1
        END
        
    ) / COUNT(id)::float * 100.0 AS percents

FROM new_payments
WHERE mode != 'Не определено'
GROUP BY 1, 2
ORDER BY 1 ASC, 2 ASC
