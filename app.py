import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Streamlit App", layout="wide")

st.sidebar.header("Settings")
name = st.sidebar.text_input("Name", "User")
data_size = st.sidebar.slider("Data Points", 10, 100, 50)

st.title(f"Dashboard for {name}")

df = pd.DataFrame(
    np.random.randn(data_size, 3),
    columns=['Metric A', 'Metric B', 'Metric C']
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Raw Data")
    st.dataframe(df)

with col2:
    st.subheader("Visual Analysis")
    st.line_chart(df)

if st.button("Process Data"):
    with st.status("Working...", expanded=True) as status:
        time.sleep(1)
        st.write("Analyzing patterns...")
        time.sleep(1)
        status.update(label="Complete", state="complete", expanded=False)
    st.balloons()
