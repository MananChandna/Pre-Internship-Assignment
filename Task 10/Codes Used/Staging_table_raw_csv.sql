CREATE TABLE IF NOT EXISTS staging_sales (
  store            INTEGER,
  date             DATE,
  weekly_sales     NUMERIC(14,2),
  holiday_flag     SMALLINT,
  temperature      REAL,
  fuel_price       NUMERIC(6,3),
  cpi              REAL,
  unemployment     REAL
);
