'''
Backend part of Text2Podcast
written by Christoferis c 2020
Notes:
-implement single gtts processing


'''

#external Imports
from pytesseract import image_to_string as imgstr
from PIL import Image
from gtts import gTTS


class backend_process:
    
    def __init__(self):
        print("instanced")
        pass
    
    def image_processing(self, file):
        data = Image.open(file)
        text = imgstr(data)
        return text
        
    def text_to_audio(self, maintext, lang):
        gTTS(text=maintext, lang=lang)