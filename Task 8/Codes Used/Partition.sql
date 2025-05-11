DO $$
DECLARE
  yr int;
BEGIN
  FOR yr IN 1979..1998 LOOP
    EXECUTE format($fmt$
      CREATE TABLE fx_rates_%1$s
        PARTITION OF fx_rates
        FOR VALUES FROM ('%1$s-01-01') TO ('%1$s-12-31');
      $fmt$, yr);
  END LOOP;
END $$;
