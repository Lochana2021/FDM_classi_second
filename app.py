#import libraries
import numpy as np
import pandas as pd
from flask import Flask, render_template,request
import pickle#Initialize the flask App

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
#default page of our web-app
@app.route('/')
def home():
    

    return render_template('classification.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    

    return render_template('classification.html')

if __name__ == "__main__":
    app.run(debug=True)

