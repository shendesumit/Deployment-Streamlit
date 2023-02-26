import streamlit as st
import numpy as numpy
import pandas as pd

st.title('Open Pub Application')
st.text('')
st.subheader('**Explore the basic information and statistics of pub dataset**:point_down:')

df = pd.read_csv('data/pub.csv')

basic = st.selectbox('',('No. of pubs in UK','Head','Tail','unique local authority','check_null_values'))

if basic=='No. of pubs in UK':
    st.markdown(f'There  are  **{df.shape[0]}**  Pubs  in  **United Kingdom**')


elif basic=='Head':
    st.dataframe(df.head())

elif basic=='Tail':
    st.dataframe(df.tail())

elif basic=='unique local authority':
    st.text(f'Total no of pub local authority is {len(df.local_authority.unique())} in United Kingdom')

elif basic=='check_null_values':
    st.markdown('**We can see that there are no null values in our dataset**')
    st.text(df.isnull().sum())

st.text('')
st.text('')

st.subheader('Find the Statistics information of the pub dataset')

stat = st.button('Describe')

if stat==True:
    st.dataframe(df.describe())
else:
    st.text('')





