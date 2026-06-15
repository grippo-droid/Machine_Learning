import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

#import ridge regressor and standard scaler pickle
import os
ridge_model=pickle.load(open(os.path.join(os.path.dirname(__file__), 'artifacts', 'ridge.pkl'), 'rb'))
standard_scaler=pickle.load(open(os.path.join(os.path.dirname(__file__), 'artifacts', 'scaler.pkl'), 'rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdatapoint',methods=['GET','POST'])
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == "POST":

        gender = float(request.form.get('gender'))
        race_ethnicity = int(request.form.get('race_ethnicity'))

        group_A = 0
        group_B = 0
        group_C = 0
        group_D = 0
        group_E = 0

        if race_ethnicity == 0:
            group_A = 1
        elif race_ethnicity == 1:
            group_B = 1
        elif race_ethnicity == 2:
            group_C = 1
        elif race_ethnicity == 3:
            group_D = 1
        else:
            group_E = 1        
        parental_level_of_education = float(request.form.get('parental_level_of_education'))
        lunch = float(request.form.get('lunch'))
        test_preparation_course = float(request.form.get('test_preparation_course'))
        reading_score = float(request.form.get('reading_score'))
        writing_score = float(request.form.get('writing_score'))

        data = [[
            gender,
            parental_level_of_education,
            lunch,
            test_preparation_course,
            reading_score,
            writing_score,
            group_A,
            group_B,
            group_C,
            group_D,
            group_E
        ]]

        scaled_data = standard_scaler.transform(pd.DataFrame(data))

        prediction = ridge_model.predict(scaled_data)

        result = round(prediction[0], 2)

        return render_template('home.html', result=result)

    else:
        return render_template('home.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0")