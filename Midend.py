'''
gTTS Integration for Text2Podcast
developed by Christoferis c 2020

TODO:
-Multithreading
'''
#Local Imports

#Ext imports
from Backend import image_processing, text_to_audio, rangen, paths
from pydub import AudioSegment
from os import startfile, getcwd
from os.path import abspath


#Note: Every part of text must be read in the language i.e in the end must merge audio
class midend:
     
    def __init__(self, files):
        self.files = files
        self.paths = list()
        self.sort_data()


    def sort_data(self):
        #Iterate over Dict keys
        for data in self.files:
            file = None

            #Checks for Image
            if data.find(".png") != -1 or data.find(".jpg") != -1 or data.find(".jpeg") != -1:
                text = image_processing(data) + "\n"
                file = text_to_audio(text, self.files.get(data))

            #text file test
            elif data.find(".txt") != -1:
                text = open(data, mode="r", encoding="utf8").read()
                file = text_to_audio(text, self.files.get(data))

            #Append to file list
            self.paths.append(file)
        #Render
        self.join_audio()

    def join_audio(self):
        #set FFMpeg and prepping
        AudioSegment.converter = paths(False)
        AudioSegment.ffmpeg = paths(False)
        final_audio = AudioSegment.empty()

        #sort list for empty strings
        
        for path in self.paths:
            try:
                self.paths.remove("")
            except Exception:
                break
        

        #Loop and add to final file
        for file in self.paths:
            audio_open = AudioSegment.from_mp3(abspath(file))
            final_audio += audio_open

        #File Name + Export
        final_name = rangen(False)
        #export + play
        final_audio.export(final_name, format="mp3")
        startfile(abspath(final_name))


