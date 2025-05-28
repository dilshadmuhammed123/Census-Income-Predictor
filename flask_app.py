from flask import Flask, render_template ,request
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickle.load(open("classification_model.pkl","rb"))

@app.route('/')
def home():
    return render_template('form.html',prediction='')
@app.route('/predict',methods=['POST'])

def index():
    input_data = {
    'age': int(request.form["age"]),
    'education': request.form['education'],
    'education-num': int(request.form["education-num"]),
    'capital-gain': int(request.form["capital-gain"]),
    'capital-loss': int(request.form["capital-loss"]),
    'hours-per-week': int(request.form["hours-per-week"]),
    'relationship_Husband': request.form["relationship_Husband"],
    'relationship_Wife': request.form["relationship_Wife"]
}
    input_df = pd.DataFrame([input_data])
    input_df['education']=input_df['education'].map({'Preschool':0,'1st-4th':1,'5th-6th':2,'7th-8th':3,'9th':4,'10th':5,'11th':6,'12th':7,
                                     'HS-grad':8,'Some-college':9,'Assoc-voc':10,'Assoc-acdm':11,'Bachelors':12,
                                     'Masters':13,'Prof-school':14,'Doctorate':15})
    
    
    predicted_class=model.predict(input_df)
    if predicted_class==0:
        predict="Income is less than 50k"
    else:
        predict="Income is greater than 50k"
        
    return render_template('form.html',prediction=predict)
if __name__ == '__main__':
    app.run(debug=True)