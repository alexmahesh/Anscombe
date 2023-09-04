
# 
# Programmed by alexmahesh
#

# import libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# Config streamlit output
st.set_page_config(layout='wide')

# load data
df = pd.read_csv('data/anscombe.csv')

st.title('Anscombe Quartet Dataset')
st.markdown("""
            The Anscombe Quartet Dataset consists of four datasets that have nearly identical
descriptive statistics but very different charts.  
It was created by 1973 by the statistician Francis Anscombe to show (among others) the 
importance of using graphics/charts in data analysis.  

In this small example I show how to use Pandas, Plotly and Streamlit to do a 
quick EDA on the Anscombe Quartett.  
You can choose one of the four datasets and see how similar their values and descriptive
statistics are but how different their drawn charts looks.  

If you want to have a look at the Python code, you can find it here: [Repository](https://github.com/alexmahesh/Anscombe).  

You can read more about Francis Anscombe and his dataset on [Wikipedia](https://en.wikipedia.org/wiki/Anscombe%27s_quartet).  
You can learn more about the Python Pandas library here: [Pandas](https://pandas.pydata.org/).  
You can learn more about the Streamlit library on: [Streamlit](https://docs.streamlit.io/).  
You can learn more about Plotly on: [Plotly](https://plotly.com/python/).  
            """)

# Interactive Data Chooser
st.subheader('Choose the dataset to display:')
# dataset = st.selectbox('Dataset', options=['1', '2', '3', '4'])
# dataset = st.slider('Dataset', min_value=1, max_value=4, value=1)
# dataset = st.number_input('Dataset', min_value=1, max_value=4, value=1)
dataset = st.radio('Dataset', options=['1', '2', '3', '4'], horizontal=True)


# prepare data
table = df[[f"x{dataset}", f"y{dataset}"]]
fig = px.scatter(df, x=f'x{dataset}', y=f"y{dataset}")

# display result

col1, col2, col3 = st.columns([0.2, 0.15, 0.6])
with col1:
    st.markdown(f"__Values of dataset {dataset}:__", unsafe_allow_html=True)
    st.dataframe(table, use_container_width=True, hide_index=True)
with col2:
    st.markdown(f"__Statistics of dataset {dataset}:__", unsafe_allow_html=True)
    st.write(table.describe())
with col3:
    st.markdown(f"__Chart of dataset {dataset}:__", unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True)
