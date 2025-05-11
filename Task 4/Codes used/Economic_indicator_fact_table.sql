CREATE TABLE fact_economics (
    country_id INT REFERENCES dim_country(country_id),
    date_id INT REFERENCES dim_date(date_id),
    inflation_rate NUMERIC,
    gdp_growth_rate NUMERIC,
    unemployment_rate NUMERIC,
    interest_rate NUMERIC,
    stock_index_value NUMERIC
);
