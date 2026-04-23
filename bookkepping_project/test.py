import pdfplumber
import pandas as pd
import numpy as np

df = pd.read_excel('D://test.xlsx')
print("LOADED  FILE:")
print(df.head())
print("=====================================")

column_mapping = {
 'Date': 'date',
 'Transaction Date': 'date',
 'Description': 'description',
 'Memo': 'description',
 'Amount': 'amount',
 'Debit': 'debit',
 'Credit': 'credit'
}

df.rename(columns=column_mapping, inplace=True)
#df = df.rename(columns=column_mapping)

df['date'] = pd.to_datetime(df['date'], errors='coerce')

if 'debit' in df.columns and 'credit' in df.columns:
    df['amount'] = df['credit'].fillna(0) - df['debit'].fillna(0)
    df.drop(['debit', 'credit'], axis=1, inplace=True)

df['description'] = df['description'].str.strip().str.upper()
df = df.sort_values('date').reset_index(drop=True)
print("\nAFTER PROCESSING")
print(df)
