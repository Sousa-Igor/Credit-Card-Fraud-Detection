WITH period AS ( 
    SELECT
        transaction_id,
        CASE 
            WHEN time_of_day_hour BETWEEN 6 AND 11 THEN 'Manha'
            WHEN time_of_day_hour BETWEEN 12 AND 17 THEN 'Tarde'
            WHEN time_of_day_hour BETWEEN 18 AND 23 THEN 'Noite'
            WHEN time_of_day_hour BETWEEN 00 AND 5 THEN 'Madrugada'
        END AS transaction_period
    FROM credit
),

velocity AS (
    SELECT
        transaction_id,
        velocity_score >= 19.8 AS is_high_velocity
    FROM credit
),

recentily AS (
    SELECT
        transaction_id,
        hours_since_last_txn <= 1 AS recentily_last_txn 
    FROM credit
),

dispute_age AS (
    SELECT
        transaction_id,
        1. * prior_disputes / card_age_months AS dispute_x_age
    FROM credit
)

SELECT
    t1.transaction_id,
    t2.transaction_period,
    t3.is_high_velocity,
    t4.recentily_last_txn,
    t5.dispute_x_age

FROM credit as t1

LEFT JOIN period as t2
ON t1.transaction_id = t2.transaction_id

LEFT JOIN velocity as t3
ON t1.transaction_id = t3.transaction_id

LEFT JOIN recentily as t4
ON t1.transaction_id = t4.transaction_id

LEFT JOIN dispute_age as t5
ON t1.transaction_id = t5.transaction_id


