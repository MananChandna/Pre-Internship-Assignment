CREATE TABLE IF NOT EXISTS dim_date (
  date_key   INTEGER     PRIMARY KEY,  -- YYYYMMDD
  date       DATE        NOT NULL,
  week       SMALLINT    NOT NULL,
  month      SMALLINT    NOT NULL,
  quarter    SMALLINT    NOT NULL,
  year       INTEGER     NOT NULL
);
