import streamlit as st
import pandas as pd
import numpy as np

# 1. Load your CSV first
df = pd.read_csv('SchoolSite_gdb_-5745748764799769002.csv')

# 2. THEN you can print columns
st.write("Columns:", df.columns.tolist())

# 3. Create LEVEL if missing
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

if 'LEVEL' not in df.columns:
    df['LEVEL'] = df['GRADES'].apply(extract_level)

# 4. Create UTILIZATION_RATE if missing
if 'UTILIZATION_RATE' not in df.columns:
    df['UTILIZATION_RATE'] = df['ENROLLMNT'] / df['CAPACITY'].replace(0, np.nan)

# 
