SELECT 
    transaction_id,
    amount_usd / account_balance_usd AS amount_balance,
    amount_usd > AVG(amount_usd) OVER() AS high_txt_amount_usd,
    txn_count_last_24h > AVG(amount_usd) OVER() AS high_volume
FROM credit

