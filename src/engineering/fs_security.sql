SELECT
    transaction_id,
    cvv_retry_count > 2 AS high_cvv_retry,
    used_vpn + ip_country_mismatch + is_new_merchant + billing_shipping_mismatch + cvv_retry_count AS high_risk,
    used_vpn = 1 AND is_foreign_transaction = 1 AS foreign_vpn,
    used_vpn = 1 AND ip_country_mismatch = 1 AS vpn_ip_mismatch

FROM credit