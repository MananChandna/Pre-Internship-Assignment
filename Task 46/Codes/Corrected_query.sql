WITH cte1 AS (
    SELECT DISTINCT countrycode, name
    FROM city
),
cte2 AS (
    SELECT 
        name, 
        population, 
        countrycode,
        ROW_NUMBER() OVER (
            PARTITION BY countrycode 
            ORDER BY population DESC
        ) AS Rn
    FROM city
)
SELECT
    cte2.population,
    cte2.name AS CityName,
    cte1.name AS CountryName
FROM cte1
JOIN cte2 
  ON cte2.countrycode = cte1.countrycode
WHERE cte2.Rn = 1;
