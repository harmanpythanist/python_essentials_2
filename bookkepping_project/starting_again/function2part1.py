import pandas as pd
import numpy as np
from datetime import datetime
import pdfplumber

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
        'Memo': 'description',
        'Amount': 'amount',
        'Debit': 'debit',
        'Credit': 'credit'
    }
    
    df.rename(columns=column_mapping, inplace=True)
    
    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    # Combine debit/credit into single amount column if needed
    if 'debit' in df.columns and 'credit' in df.columns:
        df['amount'] = df['credit'].fillna(0) - df['debit'].fillna(0)
        df.drop(['debit', 'credit'], axis=1, inplace=True)
    
    # Clean description field
    df['description'] = df['description'].str.strip().str.upper()
    
    return df.sort_values('date').reset_index(drop=True)



def extract_from_pdf(pdf_path):
    """
    Extract transaction data from PDF bank statements
    """
    transactions = []
    
    with pdfplumber.open(pdf_path) as pdf:    # pdf.pages -> all pages in a list
        for page in pdf.pages:
            text = page.extract_text()
            # Parse text based on your bank's format
            # This is a simplified example
            lines = text.split('\n')        # lines = ["line1", "line2", "line3"......, "last line"]
            for line in lines:
                # Custom parsing logic for your bank's format
                parts = line.split()   # parts = ["word1", "word2".....]
                if len(parts) >= 3:
                    transactions.append({
                        'date': parts[0],
                        'description': ' '.join(parts[1:-1]),
                        'amount': parts[-1]
                    })
    
    return pd.DataFrame(transactions)

hmara_pdf = extract_from_pdf("D://test.pdf")
hmara_pdf.to_csv("pdf.csv")
print(hmara_pdf)


'''
# Import transactions from multiple sources
bank_transactions = import_bank_transactions('bank_statement.csv', 'csv')
credit_card = import_bank_transactions('credit_card.xlsx', 'excel')

# Combine all transactions
all_transactions = pd.concat([bank_transactions, credit_card], ignore_index=True)
print(f"Total transactions imported: {len(all_transactions)}")
'''
