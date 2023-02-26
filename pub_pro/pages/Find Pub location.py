import numpy as np
import pandas as pd
import streamlit as st


st.title('Pub Location')
df = pd.read_csv('data/pub.csv')
btn_map = st.button("Display Map ")

if btn_map==True:
    st.map(df)




st.subheader('select a Local Authority')


local = df.local_authority.unique()
option = st.selectbox('',local)


'You Selected : ' ,option

btn_clk = st.button('Find now')
if btn_clk==True:
    res = df[df['local_authority']==option]
    res=res[['latitude','longitude']]
    st.map(res)
    st.markdown('_Its displaying all the pubs in the area that you selected_') 





