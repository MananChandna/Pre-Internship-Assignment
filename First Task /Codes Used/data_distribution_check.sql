SELECT 
  tableoid::regclass AS partition,
  COUNT(*) AS row_count,
  MIN(transaction_date) AS first_date,
  MAX(transaction_date) AS last_date
FROM bank_transactions
GROUP BY partition
ORDER BY first_date;
