import pandas as pd

file = 'bankdataset.xlsx'
chunk_size = 100_000
header = pd.read_excel(file, nrows=0).columns

for i in range(0, 11):  # 11 chunks for ~1M rows
    df = pd.read_excel(
        file,
        skiprows=i * chunk_size,
        nrows=chunk_size,
        header=0,
        parse_dates=['Date'],
        dtype={'Domain': 'category', 'Location': 'category', 'Value': 'int32', 'Transaction_count': 'int32'}
    )
    if df.empty: break
    df.to_csv(f'bank_data_part_{i}.csv', index=False, header=(i == 0))
