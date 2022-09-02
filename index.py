import streamlit as st
import joblib
import sklearn
import pandas as pd
import numpy as np
import pickle
from os.path import dirname, join, realpath
from sklearn import preprocessing



# add banner image
st.header("MAIZE SALES PREDICTION ON DODOMA REGION IN TANZANIA")
st.image("images/maize.jpg")


# form to collect information
my_form = st.form(key="maize_sales_prediction_form")


sales = ['medium sales' 'high sales' 'low sales']
 
Q1 = my_form.number_input('Enter Temperature',min_value=0, max_value=60)

Q2=my_form.selectbox(
    'Enter Mounth',
    (
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    )
)

def prepare_inputs(value):
    if value == 'January':
        return 0
    elif value == 'February':
        return 1
    elif value == 'March':
        return 2
    elif value == 'April':
        return 3 
    elif value == 'May':
        return 4
    elif value == 'June':
        return 5
    elif value == 'July':
        return 6
    elif value == 'August':
        return 7
    elif value == 'September':
        return 8
    elif value == 'October':
        return 9
    elif value == 'November':
        return 10
    else:
        return 11




	

submit = my_form.form_submit_button(label="Make Prediction")


model = joblib.load(open("model/maize_model.pkl", "rb"))



# result dictionary




if submit:

    # collect inputs
    input = {
        "Q1": Q1,
        "Q2": prepare_inputs(Q2)
       
    }

    # Create a DataFrame
    data = pd.DataFrame(input, index=[0])

    data = data.to_numpy()

    
    
    # perform prediction
    maize_price = model.predict(data)
    if maize_price[0] == 0:

        st.write("Maize price in {} is Low sales".format(Q2))
    elif maize_price[0] == 1:
        st.write("Maize price in {} is  medium sales".format(Q2)) 

    elif maize_price[0] == 2:
        st.write("Maize price in {} is  medium sales".format(Q2))


    





st.write("All rights are preserved  ❤️ by Mzenzi Jr Data scientist")