SELECT 
    transaction_id,
    day_of_week IN (0,6) AS is_weekend,
    time_of_day_hour BETWEEN 8 AND 17 AS is_business_hour

FROM credit