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
        df = extract_from_pdf(file_path)   # TO be done!
        
    return df


file = import_bank_transactions("D://test.csv", "csv")
print(file)





