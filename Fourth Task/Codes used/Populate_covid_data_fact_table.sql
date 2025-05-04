INSERT INTO fact_covid (country_id, total_cases, total_deaths, total_recovered, active_cases, total_tests, population)
SELECT
    dc.country_id,
    scw.total_cases,
    scw.total_deaths,
    scw.total_recovered,
    scw.active_cases,
    scw.total_tests,
    scw.population
FROM stg_covid_worldwide scw
JOIN dim_country dc ON dc.country_name = scw.country;
