import numpy as np
import pandas as pd
import joblib

__model=None

def load_save_artifects():
    print("Loading Saved Artifects ..... Start")
    global __model
    if __model is None:
        with open("saved_model.pkl",'rb') as f:
            __model=joblib.load(f)
    print("Loading Saved Artifects....Done")

def classify(gender,age,hyper_tension,heart_disease,bmi,hba1c,blood_glucose):
    l=[]
    if gender.title()=='Female':
        l.append(1)
    elif gender.title()=='Other':
        l.append(2)
    else:
        l.append(0)
    tension=1 if hyper_tension.title()=='Yes' else 0
    heart_prob=1 if heart_disease.title() == 'Yes' else 0
    gender=l[0]
    age=age/100
    bmi=bmi/100
    blood_glucose=blood_glucose/100
    value= __model.predict([[gender,age,tension,heart_prob,bmi,hba1c,blood_glucose]]) 
    prob=__model.predict_proba([[gender,age,tension,heart_prob,bmi,hba1c,blood_glucose]])
    return value,prob
if __name__ == "__main__":
    pass
    