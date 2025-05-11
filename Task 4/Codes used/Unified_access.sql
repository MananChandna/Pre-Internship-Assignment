CREATE VIEW view_country_snapshot AS
SELECT
    dc.country_name,
    dd.year,
    dd.month,
    fe.inflation_rate,
    fe.gdp_growth_rate,
    fe.unemployment_rate,
    fe.interest_rate,
    fe.stock_index_value,
    fc.total_cases,
    fc.total_deaths,
    fc.total_recovered,
    fc.active_cases,
    fc.total_tests,
    fc.population
FROM fact_economics fe
JOIN dim_country dc ON fe.country_id = dc.country_id
JOIN dim_date dd ON fe.date_id = dd.date_id
JOIN fact_covid fc ON fc.country_id = dc.country_id
WHERE dd.year = 2023;
