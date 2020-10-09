'''
Backend part of Text2Podcast
written by Christoferis c 2020
'''

#external Imports
from pytesseract import image_to_string as imgstr
from PIL import Image

class backend:
    
    def __init__(self, file):
        #Path to txt file dump
        self.file = file
        string = imgstr(self.queue)
