
from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel
import pandas as pd




app = FastAPI()




class Item(BaseModel):

    name: str

    price: float

    is_offer: Union[bool, None] = None




@app.get("")

def read_root():

    return {"Hello": "World"}




@app.get("/items/{item_id}")

def read_item(item_id: int, q: Union[str, None] = None):

    return {"item_id": item_id, "q": q}




@app.put("/items/{item_id}")

def update_item(item_id: int, item: Item):

    return {"item_name": item.name, "item_id": item_id}

# Predict endpoint
@app.get("/inference")
def predict (age,gender,height,):
    """
    Age of the Patient
    Gender of the Patient
    Height of the patient
    """
# Prepare the feature and structure them like in the notebook
data = pd.DataFrame({
    "age":[age],
    "gender":[gender],
    "height":[height],
})

print(f"[Info] The initial and raw df : {data.to_markdown()}")

# Feature Preprocessing and Creation
df_scaled = scaler.transform(data)
df_encoded = encoder.transform(data['categorical features'])

#Merging the datasets
df_cleaned = pd.concat([df_scaled,df_encoded],axis=1)

# Prediction
raw_prediction = model.predict(df_cleaned)

# Format the prediction to send to the API's reply
output = {
    "features" : {
        "age" : age,
        "gender": gender,
        "height": height,
    },
      "df" : df, #Pandas is now automatically converted, 
    "array" : df.toarray().tolist()

}