'''
gTTS Integration for Text2Podcast
developed by Christoferis c 2020

TODO:
- Make this file to the root file
- File sorter and combiner

'''
from gtts import gTTS
from OCRcomp import ocr


class root:

    def __init__(self, files):
        self.files = files
        self.extractdata = str()
        self.sort()
        pass
    
    def sort(self):
        for file in self.files:
            if file in ".txt":
                #Open file and append it to string
                pass
            elif file in (".jpg", ".jpeg", ".JPG", ".JPEG", ".png", ".PNG"):
                #send file to OCRComp
                pass
    
    def gttsInteg(self):
        pass

