from typing import Union
from model3 import generate

from fastapi import FastAPI, File, UploadFile
app = FastAPI()


#@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Save the uploaded file to a specific location
    with open(f"uploaded_files/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())
    
    # prompt = f"Based on the following text, generate 10 multiple choice questions\n{contents}"
    responses = generate(buffer.read())
    for response in responses:
        print(response.text, end="")
        
    return {"filename": file.filename}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}