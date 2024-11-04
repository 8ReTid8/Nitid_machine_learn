import streamlit as st
import pandas as pd
import numpy as np
st.title("""facebook AI""")
st.write("""my hello""")

x_value = st.slider("Select x value", 0.0, 1.0, 0.5)  # default value set to 0.5
y_value = st.slider("Select y value", 0.0, 1.0, 0.5)  # default value set to 0.5

chart_data = pd.DataFrame({"x": [x_value], "y": [y_value]})

# Scatter plot
st.write("Scatter Plot with Single Point")
st.write(chart_data)
st.vega_lite_chart(chart_data, {
    'width': 700, 
    'height': 600, 
    'mark': {'type': 'point', 'size': 100},
    'encoding': {
        'x': {'field': 'x', 'type': 'quantitative', 'scale': {'domain': [0, 1]}},
        'y': {'field': 'y', 'type': 'quantitative', 'scale': {'domain': [0, 1]}}
    }
})


