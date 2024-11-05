import streamlit as st
import pandas as pd
import numpy as np

st.title("""facebook AI""")

col1, col2 = st.columns(2)
with col1:
    x_value = st.slider("Select x value", 0.0, 10.0, 5.0, step=0.0001)

with col2:
    x_value = st.number_input("Insert x value", value=x_value)

with col1:
    y_value = st.slider("Select y value", 0.0, 10.0, 5.0, step=0.0001)

with col2:
    y_value = st.number_input("Insert y value", value=y_value)

cold1, cold2, cold3 = st.columns(3)
with cold1:
    dateinput = st.selectbox(
        "select day",
        ("sunday","monday","tuesday","wednesday","thursday","friday","saturday"),
    )
with cold2:
    monthinput = st.selectbox(
        "select month",
        (1,2,3,4,5,6,7,8,9,10,11,12),
    )
with cold3:
    hourinput = st.number_input("Insert hour", min_value=0, max_value=23, step=1, format="%d")


cols1, cols2 = st.columns(2)
chart_data = pd.DataFrame({"x": [x_value], "y": [y_value]})
with cols1:
    st.write(chart_data)
with cols2:
    st.markdown(f"<p style='font-size:21px'>Day: {dateinput} | Month: {monthinput} | Hour: {hourinput}</p>", unsafe_allow_html=True)

st.vega_lite_chart(chart_data, {
    'width': 700, 
    'height': 600, 
    'mark': {'type': 'point', 'size': 100},
    'encoding': {
        'x': {'field': 'x', 'type': 'quantitative', 'scale': {'domain': [0, 10]}},
        'y': {'field': 'y', 'type': 'quantitative', 'scale': {'domain': [0, 10]}}
    }
})

match dateinput:
    case "sunday":
        dayinput=0 
    case "monday":
        dayinput=1 
    case "tuesday":
        dayinput=2 
    case "wednesday":
        dayinput=3 
    case "thursday":
        dayinput=4 
    case "friday":
        dayinput=5 
    case "saturday":
        dayinput=6
    
if st.button("Predict",type="primary"):
    st.write("Location :")


    