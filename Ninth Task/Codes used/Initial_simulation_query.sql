EXPLAIN ANALYZE
SELECT user_id, product_name, price, rating
FROM user_products
WHERE product_id = 42
ORDER BY rating DESC
LIMIT 20 OFFSET 10000;
