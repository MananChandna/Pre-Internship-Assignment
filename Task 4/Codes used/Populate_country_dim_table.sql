INSERT INTO dim_country (country_name)
SELECT DISTINCT country FROM stg_covid_worldwide
UNION
SELECT DISTINCT country FROM stg_economic_indicators
ON CONFLICT DO NOTHING;
