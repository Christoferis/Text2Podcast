'''
Backend part of Text2Podcast
written by Christoferis c 2020
Notes:
-implement single gtts processing

'''

#External Imports
from pytesseract import image_to_string as imgstr, pytesseract as tess
from PIL import Image
from gtts import gTTS
from random import randint, choice
from json import loads

#path finder for the config file (paths.json)
def paths(type):
    #open config
    file = open("paths.json")
    cfg = loads(file.read())

    if type:
        #if true return tesseract path else ffmpeg path
        path = cfg["tesseract"]
    else:
        path = cfg["ffmpeg"]

    #close file
    file.close()
    return path

#pytesseract integration
def image_processing(file):
    #set tesseract
    tess.tesseract_cmd = paths(True)

    #read file
    data = Image.open(file)
    text = imgstr(data)
    return text

#gTTS integration
def text_to_audio(maintext, lang):
    #if no language is specified (pot Bug)
    if lang == "":
        lang = "en"

    #random tld
    tld = choice(["com", "de", "co.uk", "fr", "pt"])
    #render + filename
    audio = gTTS(text=maintext, lang=lang, tld=tld)
    filename = rangen(True)
    #save audio
    audio.save(filename)
    return filename

#File name Generator
#True = Filename for temp False for Final
def rangen(state):
    #if state true -> temp audio else -> final audio
    if state == bool(True):
        Filename = r"temp\audio"
    else:
        Filename = r"fin\audio"

    for i in range(2):
        Filename += str(randint(0, 999))
    Filename += ".mp3"
    return str(Filename)
