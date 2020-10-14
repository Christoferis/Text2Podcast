'''
gTTS Integration for Text2Podcast
developed by Christoferis c 2020

TODO:
- File sorter and combiner
-Multithreading
-Audio Merger
'''
from Backend import backend_process

#Note: Every part of text must be read in the language i.e in the end must merge audio
#Installs FFMPEG Py
class midend:

    def __init__(self, files):
        self.files = files
        self.backend = backend_process()

        self.sort()
    
    def sort(self):
        #Iterate over Dict keys
        for data in self.files:
            #Checks for Image
            if data.find(".jpg") or data.find(".jpeg") or data.find(".png"):
                text = self.backend.image_processing(data) + "\n"

            elif data.find(".txt"):
                pass
                #process text