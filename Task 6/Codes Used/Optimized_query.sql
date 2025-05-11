WITH user_summary AS (
  SELECT
    username,
    COUNT(*) AS total_user_posts,
    COUNT(DISTINCT subreddit) AS total_subreddits
  FROM reddit_activity
  GROUP BY username
  ORDER BY total_user_posts DESC
  LIMIT 100
)
SELECT
  us.username,
  rs.subreddit,
  rs.post_count,
  TO_TIMESTAMP(rs.first_utc) AS first_post,
  TO_TIMESTAMP(rs.last_utc)  AS last_post,
  (rs.last_utc - rs.first_utc)/86400.0::numeric(10,2) AS active_days,
  us.total_user_posts,
  us.total_subreddits
FROM user_summary us
JOIN LATERAL (
  SELECT
    subreddit,
    COUNT(*) AS post_count,
    MIN(utc) AS first_utc,
    MAX(utc) AS last_utc
  FROM reddit_activity
  WHERE username = us.username
  GROUP BY subreddit
  HAVING COUNT(*) > 1
  ORDER BY post_count DESC
  LIMIT 3
) rs ON true
ORDER BY
  us.total_user_posts DESC,
  us.username,
  rs.post_count DESC;
