import pandas as pd
import numpy as np
from datetime import datetime
#import pdfplumber

# Create a function that reads all files (csv, excel, pdf) from a folder automatically

#==========================================
# CALLING FUNCTIONS LATER:
#import_bank_transactions("file1", "csv")
#import_bank_transactions("file2", "excel")
#import_bank_transactions("file3", "pdf")
#==========================================


def import_bank_transactions(file_path, file_type='csv'):
    """
    Import transactions from various file formats
    """
    if file_type == 'csv':
        df = pd.read_csv(file_path)
    elif file_type == 'excel':
        df = pd.read_excel(file_path)
    elif file_type == 'pdf':
        df = extract_from_pdf(file_path)
    
    # Standardize column names
    column_mapping = {
        'Date': 'date',
        'Transaction Date': 'date',
        'Description': 'description',
        'DESC': 'description',
        'notes': 'description',
        'Memo': 'description',
        'Amount': 'amount',
        'Debit': 'debit',
        'Credit': 'credit'
    }
    
    df.rename(columns=column_mapping, inplace=True)
    
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

    #df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date
    #df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.time
    
    
    # Combine debit/credit into single amount column if needed
    if 'debit' in df.columns and 'credit' in df.columns:
        df['amount'] = df['credit'].fillna(0) - df['debit'].fillna(0)   # replace not available value with 0
        df.drop(['debit', 'credit'], axis=1, inplace=True)    # axis = 0 -> ROWS    axis = 1 -> COLUMNS
    
    
    # Clean description field
    df['description'] = df['description'].str.strip().str.upper()    #   '    UTILITY    BILLS    '   -> 'UTILITY BILL'

    
    df = df.sort_values('date').reset_index(drop=True)
    return df 
    


file = import_bank_transactions("D://test.xlsx", "excel")
print(file)





