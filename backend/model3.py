import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models


def generate(file_contents):
  vertexai.init(project="test1-418901", location="us-central1")
  model = GenerativeModel("gemini-1.0-pro-vision-001")
  text1 = """generate 10 multiple questions in json format following this schema [{"question: String, "options": String[], "answer": String}]"""
  document1 = Part.from_data(mime_type="application/pdf",
    data=file_contents)
  responses = model.generate_content(
      [text1, document1],
      #generation_config=generation_config,
      #safety_settings=safety_settings,
      stream=True,
  )

  return responses

def additional(wrong_questions):
  vertexai.init(project="test1-418901", location="us-central1")
  model = GenerativeModel("gemini-1.0-pro-vision-001")
  text1 = """The user got the ""wrong_questions wrong" wrong, generate one paragaph of the topic on each question for the student engineer or employee 
          to learn more about this safety topic, return in json format"""
  responses = model.generate_content(
    [text1],
    stream=True,
  )
  return responses