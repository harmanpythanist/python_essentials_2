import pdfplumber
import pandas as pd
import numpy as np
transactions = []
with pdfplumber.open("D://test.pdf") as pdf: 
    for page in pdf.pages: 
        text = page.extract_text()
        lines = text.split('\n') 
        for line in lines: 
            parts = line.split() 
            if len(parts) >= 3: 
                transactions.append({ 
                'date': parts[0], 
                'description': ' '.join(parts[1:-1]), 
                'amount': parts[-1] 
                })

df = pd.DataFrame(transactions)
print(df.head())
