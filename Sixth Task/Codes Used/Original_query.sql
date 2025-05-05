WITH user_sub_stats AS (
  SELECT
    username,
    subreddit,
    COUNT(*)            AS post_count,
    MIN(utc)            AS first_utc,
    MAX(utc)            AS last_utc
  FROM reddit_activity
  GROUP BY username, subreddit
),
user_summary AS (
  SELECT
    username,
    SUM(post_count)           AS total_user_posts,
    COUNT(DISTINCT subreddit) AS total_subreddits
  FROM user_sub_stats
  GROUP BY username
),
ranked_subs AS (
  SELECT
    uss.username,
    uss.subreddit,
    uss.post_count,
    TO_TIMESTAMP(uss.first_utc) AS first_post,
    TO_TIMESTAMP(uss.last_utc)  AS last_post,
    (uss.last_utc - uss.first_utc) AS active_span_secs,
    RANK() OVER (
      PARTITION BY uss.username
      ORDER BY uss.post_count DESC
    ) AS rank_within_user
  FROM user_sub_stats uss
)
SELECT
  rs.username,
  rs.subreddit,
  rs.post_count,
  rs.first_post,
  rs.last_post,
  -- cast to numeric with two decimals
  (rs.active_span_secs / 86400.0)::numeric(10,2) AS active_days,
  us.total_user_posts,
  us.total_subreddits
FROM ranked_subs rs
JOIN user_summary us
  ON rs.username = us.username
WHERE rs.rank_within_user <= 3
  AND rs.post_count > 1
ORDER BY
  us.total_user_posts DESC,
  rs.username,
  rs.post_count DESC
LIMIT 100;
