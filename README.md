# Save this as app.py if you're using Streamlit

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('SchoolSite_gdb_-5745748764799769002.csv')

# Preprocessing (assuming you already have these columns)
df['UTILIZATION_RATE'] = df['ENROLLMNT'] / df['CAPACITY'].replace(0, pd.NA)

# Sidebar Filter
level = st.sidebar.selectbox('Select School Level', ['All', 'Elementary', 'Middle', 'Senior'])

if level != 'All':
    df = df[df['GRADES'].str.contains(level, na=False)]

st.title('Miami-Dade School Enrollment Analysis')

# Top and Bottom Schools
st.subheader('Top 10 Schools by Enrollment')
st.dataframe(df.sort_values('ENROLLMNT', ascending=False)[['NAME', 'GRADES', 'CAPACITY', 'ENROLLMNT', 'UTILIZATION_RATE']].head(10))

st.subheader('Schools Over Capacity (>100%)')
overcrowded = df[df['UTILIZATION_RATE'] > 1]
st.dataframe(overcrowded[['NAME', 'GRADES', 'CAPACITY', 'ENROLLMNT', 'UTILIZATION_RATE']])

st.subheader('Schools Underutilized (<80%)')
underutilized = df[df['UTILIZATION_RATE'] < 0.8]
st.dataframe(underutilized[['NAME', 'GRADES', 'CAPACITY', 'ENROLLMNT', 'UTILIZATION_RATE']])

# Visualization
st.subheader('Top 10 Overcrowded Schools')
top_overcrowded = overcrowded.sort_values('UTILIZATION_RATE', ascending=False).head(10)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(data=top_overcrowded, x='UTILIZATION_RATE', y='NAME', palette='Reds_r', ax=ax)
plt.xlabel('Utilization Rate')
plt.ylabel('School Name')
st.pyplot(fig)

st.subheader('Utilization Rate Distribution')
fig2, ax2 = plt.subplots()
sns.histplot(df['UTILIZATION_RATE'].dropna(), bins=20, kde=True)
st.pyplot(fig2)

# Download Button
st.subheader('Download Filtered Data')
st.download_button('Download CSV', df.to_csv(index=False), 'schools_filtered.csv')
