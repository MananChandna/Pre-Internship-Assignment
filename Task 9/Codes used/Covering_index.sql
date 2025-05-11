CREATE INDEX idx_up_prod_rating
  ON user_products(product_id, rating DESC)
  INCLUDE (user_id, product_name, price);
