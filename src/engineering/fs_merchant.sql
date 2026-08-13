SELECT
    transaction_id,
    merchant_risk_score > AVG(merchant_category) OVER() AS high_risk_merchant,
    amount_usd > AVG(amount_usd) OVER() AND merchant_risk_score > AVG(merchant_category) OVER() AS high_amount_risk,
    is_new_merchant = 1 AND is_foreign_transaction = 1 AS new_foreign_merchant,
    is_new_merchant,
    is_foreign_transaction
FROM credit

