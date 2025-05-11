INSERT INTO fact_economics (country_id, date_id, inflation_rate, gdp_growth_rate, unemployment_rate, interest_rate, stock_index_value)
SELECT
    dc.country_id,
    dd.date_id,
    sei.inflation_rate,
    sei.gdp_growth_rate,
    sei.unemployment_rate,
    sei.interest_rate,
    sei.stock_index_value
FROM stg_economic_indicators sei
JOIN dim_country dc ON dc.country_name = sei.country
JOIN dim_date dd ON dd.date = sei.date;
