import streamlit as st
import numpy as np
import pandas as pd

def app():
    st.title('Data Stats')
    st.write("This is a sample data stats in the mutliapp.")
    st.write("See `apps/data_stats.py` to know how to use it.")
    st.markdown("### Plot Data")
    df= pd.DataFrame(
        np.random.rand(20,3),
        columns=['a','b','c']
    )

    st.line_chart(df)
