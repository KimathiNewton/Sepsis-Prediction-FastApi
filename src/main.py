
# Importations

from typing import Union
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd
import os
# Assuming these imports for scaler and label_encoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Setup Section
 
## A function to load machine Learning components to re-use
def Ml_loading_components(fp):
    with open(fp, "rb") as f:
        object=pickle.load(f)
        return(object)

# Loading the machine learning components
DIRPATH = os.path.dirname(os.path.realpath(__file__))
ml_core_fp = os.path.join(DIRPATH,"ML","ML_Model.pkl")
ml_components_dict = Ml_loading_components(fp=ml_core_fp)



# Defining the variables for each component
label_encoder = ml_components_dict['label_encoder']
scaler = ml_components_dict['scaler']
model = ml_components_dict['model']


# Create FastAPI instance
app = FastAPI(title="Sepsis Prediction API",description="API for Predicting Sespsis ")


# Create prediction endpoint
@app.get("/predict")
def predict (PRG:float,PL:float,BP:float,SK:float,TS:float,BMI:float,BD2:float,Age:float):

    """
* PRG: Plasma glucose

* PL: Blood Work Result-1 (mu U/ml)

* PR: Blood Pressure (mmHg)

* SK: Blood Work Result-2(mm)

* TS: Blood Work Result-3 (muU/ml)

* M11: Body mass index (weight in kg/(height in m)^2

* BD2: Blood Work Result-4 (mu U/ml)

* Age: patients age(years)


"""   
    # Prepare the feature and structure them like in the notebook
    df = pd.DataFrame({
        "PRG":[PRG],
        "PL":[PL],
        "BP":[BP],
        "SK":[SK],
        "TS":[TS],
        "BMI":[BMI],
        "BD2":[BD2],
        "Age":[Age]
    })


    print(f"[Info] The inputed dataframe is : {df.to_markdown()}")

    # Feature Preprocessing and Creation
    df_scaled = scaler.transform(df)


    # Prediction
    raw_prediction = model.predict(df_scaled)
    if raw_prediction == 0:
        return{f"The patient will Not Develop Sepsis"}
    elif raw_prediction == 1:
        return {f"The patient Will Develop Sepsis"}
    else:
        return {"Error"}


if __name__ == "__main__":
    uvicornf.run("main:app",reload=True)
