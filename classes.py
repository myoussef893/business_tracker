import streamlit as st
from model import Items,User,session
from datetime import datetime as dt 
from random import randint
import streamlit_authenticator as stauth
import gspread
import pandas as pd

gc = gspread.service_account('creds.json')
sht = gc.open('Amazon-Business')
payments_sheet = sht.worksheet('Payments')
categories = sht.worksheet('Categories')
df = pd.DataFrame(payments_sheet.get_values('A:I'))
df.columns= df.iloc[0]
df = df.drop(0).reset_index(drop=True)
df['Total Price'] = pd.to_numeric(df['Total Price'])
df['Date'] = pd.to_datetime(df['Date'],format='%d/%m/%Y')
dfg = df.groupby('Date')['Total Price'].sum().sort_index(ascending=True)
class SystemForms:
    def __init__(self) -> None:
        pass

    def add_item(self):
        with st.form(key='Scan Item Form'): 
           date = st.date_input('Purchase Date')
           product = st.selectbox('Product', options=[item[0] for item in categories.get_values('A2:A')])
           quantity = st.number_input('Quantity')
           price = st.number_input('Price: ')
           store = st.selectbox('Store', options=[item[0] for item in categories.get_values('I2:I')])
           comments = st.text_area('Comments')
           submit = st.form_submit_button('Save')

        if submit:
            date = date.strftime('%Y-%m-%d')
            payments_sheet.append_row([None,date,product,quantity,price,None,store,None,comments])
            st.success('Successfully Saved',icon='🎉')

    def signup(self): 
        with st.form(key='Signup Form'): 
            username = st.text_input('User Name')
            full_name = st.text_input('Full Name')
            email = st.text_input('email')
            password = st.text_input('password')
            submit = st.form_submit_button('Signup')

        if submit: 
            user_model = UserModel()
            user_model.add_user(username=username,full_name=full_name,email=email,password=password)
            st.success('Signed up successfully',icon='🥳')



class ItemsModel: 
    def __init__(self) -> None:
        pass


    def add_item(self,tracking_number, status,item_weight,user,country):
        new_item = Items(
            id = randint(1000,9999999), 
            tracking_number = tracking_number,
            receiving_date = str(dt.today().date()), 
            country=country,
            status = status, 
            item_weight = item_weight, 
            quantity = 1,
            item_price = 27,
            user = user
        )         
        session.add(new_item)
        session.commit()


## UserModel Updater Object
class UserModel:
    def add_user(self,username,full_name,email,password):
        new_user = User(
            id = randint(1000,9999999),
            username = username, 
            full_name = full_name, 
            email = email, 
            password = password,
        )

        session.add(new_user)
        session.commit()