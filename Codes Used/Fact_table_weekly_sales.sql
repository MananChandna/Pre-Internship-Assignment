CREATE TABLE IF NOT EXISTS fact_weekly_sales (
  date_key      INTEGER     NOT NULL
    REFERENCES dim_date(date_key),
  store_key     INTEGER     NOT NULL
    REFERENCES dim_store(store_key),
  weekly_sales  NUMERIC(14,2) NOT NULL,
  holiday_flag  SMALLINT      NOT NULL,
  temperature   REAL,
  fuel_price    NUMERIC(6,3),
  cpi           REAL,
  unemployment  REAL,
  PRIMARY KEY (date_key, store_key)
);
