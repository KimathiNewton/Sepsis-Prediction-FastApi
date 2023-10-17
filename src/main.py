
# Importations

from typing import Union
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd
import os
from fastapi import HTTPException, status
import uvicorn
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
 
# Setup Section  
  
 # Create FastAPI instance
app = FastAPI(title="Sepsis Prediction API",description="API for Predicting Sespsis ")
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
label_encoder = ml_components_dict['label_encoder'] # The label encoder
# Loaded scaler component
scaler = ml_components_dict['scaler']
#Loaded model 
model = ml_components_dict['model']
# Defining our input variables


class InputData(BaseModel):
    PRG: int
    PL: int
    BP: int
    SK: int
    TS: int
    BMI: float
    BD2: float
    Age: int

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
# Index route
@app.get("/")
def index():
    return{'message':'Hello, Welcome to My Sepsis Prediction FastAPI'}

 
# Create prediction endpoint
@app.post("/predict")
def predict (df:InputData):

 
    # Prepare the feature and structure them like in the notebook
    df = pd.DataFrame([df.dict().values()],columns=df.dict().keys())


    print(f"[Info] The inputed dataframe is : {df.to_markdown()}")
    age = df['Age']
    print(age)
    # Scaling the inputs
    df_scaled = scaler.transform(df)


    # Prediction
    raw_prediction = model.predict(df_scaled)

    if raw_prediction == 0:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The patient does not have Sepsis")
    elif raw_prediction == 1:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The patient has Sepsis")
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction Error")


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)

# Importations
    
from typing import Union
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd
import os
import uvicorn
from fastapi import HTTPException, status

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
# Setup Section
  
 # Create FastAPI instance
app = FastAPI(title="Sepsis Prediction API",description="API for Predicting Sespsis ")
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
label_encoder = ml_components_dict['label_encoder'] # The label encoder
# Loaded scaler component
scaler = ml_components_dict['scaler']
#Loaded model 
model = ml_components_dict['model']
# Defining our input variables


class InputData(BaseModel):
    PRG:int
    PL: int
    BP: int
    SK: int
    TS: int
    BMI: float
    BD2: float
    Age: int

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
# Index route
@app.get("/")
def index():
    return{'message':'Hello, Welcome to My Sepsis Prediction FastAPI'}

 
# Create prediction endpoint
@app.post("/predict")
def predict (df:InputData):

  
    # Prepare the feature and structure them like in the notebook
    df = pd.DataFrame([df.dict().values()],columns=df.dict().keys())


    print(f"[Info] The inputed dataframe is : {df.to_markdown()}")
    age = df['Age']
    print(age)
    # Scaling the inputs
    df_scaled = scaler.transform(df)


    # Prediction
    raw_prediction = model.predict(df_scaled)

    if raw_prediction == 0:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The patient will Not Develop Sepsis")
    elif raw_prediction == 1:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="The patient Will Develop Sepsis")
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Prediction Error")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7860, reload=True)










