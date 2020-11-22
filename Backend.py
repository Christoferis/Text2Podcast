'''
Backend part of Text2Podcast
written by Christoferis c 2020
Notes:
-implement single gtts processing

'''

#External Imports
from pytesseract import image_to_string as imgstr, pytesseract
from PIL import Image
from gtts import gTTS
from random import randint, choice

#pytesseract integration
def image_processing(file):
    data = Image.open(file)
    text = imgstr(data)
    return text

#gTTS integration
def text_to_audio(maintext, lang):
    tld = choice(["com", "de", "co.uk", "fr", "pt"])
    audio = gTTS(text=maintext, lang=lang, tld=tld)
    filename = rangen(True)
    audio.save(filename)
    return filename

#File name Generator
#True = Filename for temp False for Final
def rangen(state):
    if state == bool(True):
        Filename = r"temp\audio"
    else:
        Filename = r"fin\audio"

    for i in range(2):
        Filename += str(randint(0, 999))
    Filename += ".mp3"
    return str(Filename)