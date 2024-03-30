from typing import Union

from fastapi import FastAPI

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
    return dict_new
    
    
    
    
    #return {"Hello": "World"}




@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}