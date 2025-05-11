SELECT 
    a.Buyer,
    a.ItemName AS Item_X,
    b.ItemName AS Item_Y,
    COUNT(*) AS Frequency
FROM 
    purchases a
JOIN 
    purchases b 
    ON a.Buyer = b.Buyer AND a.ItemName <> b.ItemName
GROUP BY 
    a.Buyer, a.ItemName, b.ItemName
ORDER BY 
    Frequency DESC;
