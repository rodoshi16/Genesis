from typing import Union
from model3 import generate
import os
import json
from fastapi import FastAPI, File, UploadFile
app = FastAPI()


#@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/questions/{category}')
def get_questions(category):
    #create a dict   
    dict_file = {"first_aid": "first aid.pdf", "electrical_hazards": "electrical hazards.pdf",
                 "fire_emergency": "fire emergency.pdf", "general_lab_safety": "General lab safety.pdf",
                 "report_incident": "report incident.pdf"}
    filename = dict_file.get(category) #find the file using key
    # Read the file contents
    with open(f"./categories/{filename}", "rb") as file:
        file_contents = file.read()

    # Generate responses (Replace this with your own generate function)
    # Assuming responses is a list of generated responses
    responses = generate(file_contents)  # Call your generate function with file contents

    # Print each response
    # for response in responses:
    #     print(response.text, end="")

    # # Return information about the file
    # return {"filename": filename}
    
    response_texts = []
    for response in responses:
        response_texts.append(response.text)
        # print(response.text)
    # print(len(responses))
    # return responses.to_dict()
    
    # Return the response as JSON
    return json.loads(''.join(response_texts))
    # json_string = json.dumps(my_dict)
    # return json_string

# #how to receive query parameters with fast api
# @app.post("/upload/")
# async def upload_file(file: UploadFile = File(...)):
#     # Save the uploaded file to a specific location
#     with open(f"uploaded_files/{file.filename}", "wb") as buffer:
#         buffer.write(await file.read())
    
#     # prompt = f"Based on the following text, generate 10 multiple choice questions{contents}"
#     responses = generate(buffer.read())
#     for response in responses:
#         print(response.text, end="")
        
#     return {"filename": file.filename}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
