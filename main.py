from capture_voice import get_audio
import cv2
from gemini_api import gemini_response
from playing_audio import speech_answer

while  True:
    query = get_audio()
    
    response = gemini_response(query)
    
    print(response)
    
    