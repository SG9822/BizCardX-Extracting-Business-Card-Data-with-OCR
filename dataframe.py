import pandas as pd
import streamlit as st
from edit_del import engine


def dataFrame():
    df = pd.read_sql_query("select * from images", engine)
    st.dataframe(df, use_container_width=True)
