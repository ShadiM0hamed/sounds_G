import google.generativeai as genai
import os
from deep_translator import GoogleTranslator
from snapshot import snapshot
from PIL import Image
from dotenv import dotenv_values

GEMINI_KEY = dotenv_values('.env').get('gemini_api')

genai.configure(api_key=os.getenv(GEMINI_KEY) or GEMINI_KEY)

model =  genai.GenerativeModel("gemini-pro")
vision_model = genai.GenerativeModel("models/gemini-pro-vision")

def gemini_response(query):
    en_translated_query = GoogleTranslator(source='auto', target='en').translate(query)

    response = model.generate_content("Answery briefly, \n" + en_translated_query).text

    ar_translated_rsponse = GoogleTranslator(source='auto', target='ar').translate(response)

    return ar_translated_rsponse


def gemini_vision_response(img):
    # response = vision_model.generate_content(Image.fromarray(img))  # simply pass the image
    # print(response.text)
    # #Output:
    # # Stunning!

    response = vision_model.generate_content(["where is the phone in this image?", Image.fromarray(img)])  
    # pass image and text
    print(response.text)
    
    return response.text

gemini_vision_response(snapshot())
