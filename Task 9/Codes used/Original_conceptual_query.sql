SELECT /* many columns */
FROM Users2Badges AS ub
JOIN Badges AS b       ON b.Id = ub.BadgeId
JOIN Users AS u        ON u.Id = ub.UserId
LEFT JOIN Posts AS p   ON p.Id = ub.ReasonId AND b.BadgeReasonTypeId = 2
LEFT JOIN Tags AS t    ON t.Id = ub.ReasonId AND b.BadgeReasonTypeId = 1
WHERE ub.BadgeId = @BadgeId
ORDER BY ub.Date DESC
OFFSET @Offset ROWS FETCH NEXT @PageSize ROWS ONLY;
