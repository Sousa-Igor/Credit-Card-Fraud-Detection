SELECT
    t1.*,
    t2.high_risk_merchant,
    t2.high_amount_risk,
    t2.new_foreign_merchant,
    t3.high_cvv_retry,
    t3.high_risk,
    t3.foreign_vpn,
    t3.vpn_ip_mismatch,
    t4.is_weekend,
    t4.is_business_hour,
    t5.amount_balance,
    t5.high_txt_amount_usd,
    t5.high_volume
FROM fs_customer AS t1

LEFT JOIN fs_merchant AS t2
ON t1.transaction_id = t2.transaction_id

LEFT JOIN fs_security AS t3
ON t1.transaction_id = t3.transaction_id

LEFT JOIN fs_temporais AS t4
ON t1.transaction_id = t4.transaction_id

LEFT JOIN fs_transaction AS t5
ON t1.transaction_id = t5.transaction_id
