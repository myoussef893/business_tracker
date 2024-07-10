## this is a system that will follow up on the data for my amazon store. 


import streamlit as st 
from classes import SystemForms,df,dfg
import streamlit_authenticator as stauth



amz_form = SystemForms()



def page1(): 
    st.title('Dashboard')
    st.line_chart(dfg)
    st.write(df)
    

def new_product(): 
    st.title('Add Purchased Stock')
    amz_form.add_item()


pg = st.navigation([
    st.Page(page1,title='First Page',icon="🔥"),
    st.Page(new_product,title = 'Scan New Item',icon='😊'),

])

pg.run()