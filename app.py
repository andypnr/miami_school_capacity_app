st.write("Columns:", df.columns.tolist())

import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv('SchoolSite_gdb_-5745748764799769002.csv')

# If LEVEL column is missing, create it
if 'LEVEL' not in df.columns:
    def extract_level(grades):
        grades = str(grades).upper()
        if 'PK' in grades or 'K' in grades or '1' in grades:
            return 'Elementary'
        elif '6' in grades or '7' in grades or '8' in grades:
            return 'Middle'
        elif '9' in grades or '10' in grades or '11' in grades:
            return 'High'
        else:
            return 'Other'
    df['LEVEL'] = df['GRADES'].apply(extract_level)

# If UTILIZATION_RATE is missing, create it
if 'UTILIZATION_RATE' not in df.columns:
    df['UTILIZATION_RATE'] = df['ENROLLMNT'] / df['CAPACITY'].replace(0, np.nan)

