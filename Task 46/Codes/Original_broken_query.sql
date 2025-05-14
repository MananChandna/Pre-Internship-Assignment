WITH cte1 AS (
    SELECT DISTINCT countrycode, name
    FROM city
),
cte2 AS (
    SELECT name, population
    FROM city
    WHERE cte2.countrycode = cte1.countrycode    -- incorrect reference
    ORDER BY population DESC
    LIMIT 1
)
SELECT
    population,
    name,
    name
FROM (
    SELECT *
    FROM cte1, cte2
) AS a;
