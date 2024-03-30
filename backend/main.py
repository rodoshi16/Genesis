from typing import Union

from fastapi import FastAPI
from model_service import generate

import json

app = FastAPI()


@app.get("/")
#creating an get endpoint at the root
#the frontend can access
#if i want to get a list of questions

def read_root(): #call the notebook in the genai
    #return the json answers 
    #create separate functions
    #load file
    #create prompt
    #return json
    
    #create dict
    dict_new = {"safety": "important", "next": "also"}
    response = generate()
    for question in json.dump(response).questions:
        print(question)
    return {}
    
    
    
    
    #return {"Hello": "World"}




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}