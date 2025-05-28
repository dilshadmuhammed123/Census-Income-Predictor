import streamlit as st
import pickle
import pandas as pd

with open("classification_model.pkl",'rb')as model_file:
    model=pickle.load(model_file)


st.title("income prediction")

age=st.number_input("age")
education=st.selectbox("education",["Preschool","1st-4th","5th-6th","7th-8th","9th","10th","11th","12th","HS-grad","Some-college","Assoc-voc","Assoc-acdm","Bachelors","Masters","Prof-school","Doctorate"])
education_num=st.number_input("education-num")
capital_gain=st.number_input("capital-gain")
capital_loss=st.number_input("capital-loss")
hours_per_week=st.number_input("hours-per-week")
relationship_Husband=st.number_input("relationship_Husband")
relationship_Wife=st.number_input("relationship_Wife")

input_data =pd.DataFrame({
    'age':[age],
    "education":[education],
    "education-num":[education_num],
    'capital-gain':[capital_gain],
    'capital-loss':[capital_loss],
    'hours-per-week':[hours_per_week],
    'relationship_Husband':[relationship_Husband],
    'relationship_Wife':[relationship_Wife]
  
})
edu_order = {
    'Preschool': 0, '1st-4th': 1, '5th-6th': 2, '7th-8th': 3, '9th': 4, '10th': 5, '11th': 6,
    '12th': 7, 'HS-grad': 8, 'Some-college': 9, 'Assoc-voc': 10, 'Assoc-acdm': 11,
    'Bachelors': 12, 'Masters': 13, 'Prof-school': 14, 'Doctorate': 15
}

input_data['education']=input_data['education'].map(edu_order)

if st.button("Predict Income"):
    prediction = model.predict(input_data)
    result ="> 50k "if prediction[0]==1 else "< 50k"

    st.success(f"Predicted Income is: {result}")

