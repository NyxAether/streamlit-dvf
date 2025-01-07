import time
import streamlit as st
import numpy as np
import pandas as pd

# Columns layout

left_c, right_c = st.columns(2)


# Dataframe
df = pd.DataFrame(
    np.random.randn(10,20),
    columns=(f'col {i}' for i in range(20))
)
with left_c:
    st.dataframe(df.style.highlight_max(axis=0))


    # Map
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)
    st.text_input("Your name", key="name")
    st.write("Hello", st.session_state.name)

with right_c:
# Widget
    x = st.slider('x')
    st.write(x, 'squared is', x *x)

    # Access widget by key

    # Selectbox
    col_choosen = st.sidebar.selectbox("Which column do you want ?", df.columns)
    # Line plot
    st.line_chart(df[col_choosen])


# Progress bar
latest_iteration = st.empty()
bar =st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)