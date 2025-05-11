DO $$
DECLARE partition_name text;
BEGIN
  FOR partition_name IN
    SELECT inhrelid::regclass::text
    FROM pg_inherits
    WHERE inhparent = 'bank_transactions'::regclass
  LOOP
    EXECUTE format('CREATE INDEX ON %s (transaction_date)', partition_name);
    EXECUTE format('CREATE INDEX ON %s (domain)', partition_name);
  END LOOP;
END $$;
