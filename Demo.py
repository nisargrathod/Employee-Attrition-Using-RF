import pandas as pd 
import numpy as np 
import pickle 
import streamlit as stm 
from PIL import Image 
  
# loading in the model to predict on the data 
pickle_in = open('nisarg_model.pkl', 'rb') 
classifier = pickle.load(pickle_in) 
  

stm.set_page_config(page_title="This is a Multipage WebApp") 
stm.title("Industrial Training For Govt Faculty")

status = stm.radio("Select Gender: ", ('Male', 'Female'))
if status == 'Male':
    stm.success("Male")
else:
    stm.success("Female")

category_age = stm.selectbox("Categories: ", ['Age'])
age = stm.text_input("Enter Your Age", "Type Here ...")

category_fare = stm.selectbox("Categories: ", ['Fare'])
fare = stm.text_input("Enter Ticket Fare", "Type Here ...")

stm.write("Choose Categories: ", category_age)

status_class = stm.radio("Select Passenger Class: ", ('1st-Upper', '2nd-Middle', '3rd-Lower'))
if status_class == '1st-Upper':
    stm.success("1st-Upper")
elif status_class == '2nd-Middle':
    stm.success("2nd-Middle")
else:
    stm.success("3rd-Lower")

status_embarked = stm.radio("Select Embarked Station: ", ('Cherbourg', 'Queenstown', 'Southampton'))
if status_embarked == 'Cherbourg':
    stm.success("Cherbourg")
elif status_embarked == 'Queenstown':
    stm.success("Queenstown")
else:
    stm.success("Southampton")

if stm.button('Submit'):
    to_predict_list = [age, fare, status_class, status_embarked]
    result = ValuePredictor(to_predict_list)
    prediction = 'Survived 500' if int(result) == 1 else 'Survived 100'
    stm.success(prediction)
