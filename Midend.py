'''
gTTS Integration for Text2Podcast
developed by Christoferis c 2020

TODO:
- File sorter and combiner

'''
from Backend import backend


class midend:

    def __init__(self, files):
        self.files = files
        self.finaltext = str()
        self.sort()
        pass
    
    def sort(self):
        #Iterate over Dict keys
        for data in self.files.keys:
            #Checks for Image
            if data in (".png", ".PNG", ".jpg", ".jpeg", ".JPG", "JPEG"):
                pass
