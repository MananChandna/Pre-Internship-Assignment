INSERT INTO dim_date (date, year, month, quarter)
SELECT DISTINCT
    date,
    EXTRACT(YEAR FROM date)::INT,
    EXTRACT(MONTH FROM date)::INT,
    EXTRACT(QUARTER FROM date)::INT
FROM stg_economic_indicators
ON CONFLICT DO NOTHING;
