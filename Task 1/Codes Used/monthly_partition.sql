DO $$
BEGIN
  FOR month IN 1..12 LOOP
    EXECUTE format(
      'CREATE TABLE transactions_2022_%s PARTITION OF bank_transactions
       FOR VALUES FROM (%L) TO (%L)',
      LPAD(month::text, 2, '0'),
      format('2022-%s-01', LPAD(month::text, 2, '0')),
      CASE 
        WHEN month = 12 THEN '2023-01-01'
        ELSE format('2022-%s-01', LPAD((month+1)::text, 2, '0'))
      END
    );
  END LOOP;
END $$;
