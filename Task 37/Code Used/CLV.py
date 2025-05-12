import pandas as pd

df = pd.read_csv("/content/Retail_Transaction_Dataset.csv")

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

customer_metrics = df.groupby('CustomerID').agg({
    'TotalAmount': 'sum',
    'TransactionDate': ['min', 'max', 'count']
})

customer_metrics.columns = ['TotalRevenue', 'FirstPurchase', 'LastPurchase', 'TransactionCount']

customer_metrics['AvgOrderValue'] = customer_metrics['TotalRevenue'] / customer_metrics['TransactionCount']

customer_metrics['CustomerLifespanYears'] = (
    (customer_metrics['LastPurchase'] - customer_metrics['FirstPurchase']).dt.days / 365.0
).replace(0, 1/365)  

customer_metrics['PurchaseFreqPerYear'] = customer_metrics['TransactionCount'] / customer_metrics['CustomerLifespanYears']

customer_metrics['CLV'] = customer_metrics['AvgOrderValue'] * customer_metrics['PurchaseFreqPerYear'] * customer_metrics['CustomerLifespanYears']

customer_metrics.to_csv("Customer_Lifetime_Value_Report.csv")
