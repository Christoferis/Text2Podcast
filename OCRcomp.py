'''
OCR part of Text2Podcast
Rework to work with individual Images

'''

#external Imports
from pytesseract import image_to_string as imgstr
from PIL import Image

class ocr:
    
    def __init__(self, file):
        #Path to txt file dump
        self.file = file
        string = imgstr(self.queue)
