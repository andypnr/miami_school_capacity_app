import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('SchoolSite_gdb_-5745748764799769002.csv')

# Assume LEVEL column already exists; if not, create it
# df['LEVEL'] = df['GRADES'].apply(extract_level)  # if you have a function

# Title
st.title('Miami-Dade Public Schools - Capacity vs Enrollment')

# Sidebar filter
school_level = st.sidebar.selectbox(
    "Select School Level",
    ("All", "Elementary", "Middle", "High")
)

# Filter the dataframe
if school_level == "All":
    df_filtered = df.copy()
else:
    df_filtered = df[df['LEVEL'].str.lower() == school_level.lower()]

# If no data after filtering, show message
if df_filtered.empty:
    st.warning("No data available for the selected school level.")
else:
    # Show filtered data
    st.subheader(f"Showing {school_level} Schools")
    st.dataframe(df_filtered[['NAME', 'LEVEL', 'CAPACITY', 'ENROLLMNT', 'UTILIZATION_RATE']])

    # Show Enrollment vs Capacity
    st.subheader("Enrollment vs Capacity")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=df_filtered, x='CAPACITY', y='ENROLLMNT', hue='LEVEL', palette='Set2', s=100)
    plt.plot([0, df_filtered['CAPACITY'].max()], [0, df_filtered['CAPACITY'].max()], 'k--', label='Ideal Line')
    plt.xlabel('Capacity')
    plt.ylabel('Enrollment')
    plt.title('Enrollment vs Capacity by School')
    plt.legend()
    st.pyplot(fig)

    # Top 5 Overcrowded Schools
    st.subheader("Top 5 Overcrowded Schools")
    top_overcrowded = df_filtered.sort_values(by='UTILIZATION_RATE', ascending=False).head(5)
    st.dataframe(top_overcrowded[['NAME', 'CAPACITY', 'ENROLLMNT', 'UTILIZATION_RATE']])

    # Top 5 Underutilized Schools
    st.subheader("Top 5 Underutilized Schools")
    top_underutilized = df_filtered.sort_values(by='UTILIZATION_RATE', ascending=True).head(5)
    st.dataframe(top_underutilized[['NAME', 'CAPACITY', 'ENROLLMNT', 'UTILIZATION_RATE']])
