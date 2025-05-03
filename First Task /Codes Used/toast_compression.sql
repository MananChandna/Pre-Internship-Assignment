ALTER TABLE bank_transactions
ALTER COLUMN location SET STORAGE MAIN;  -- Compress values > 2KB
