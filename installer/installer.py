'''
Installer for Text2Podcast by Christoferis
https://github.com/christoferis/text2podcast

CC BY 4.0
'''

LICENSE = '''
This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons,
PO Box 1866, Mountain View, CA 94042, USA.

'''

from tkinter import Tk, Label, Entry, Button, Frame
from tkinter.filedialog import askdirectory as diropen
from os import fspath, mkdir, system

#Instance window
main = Tk()
main.title("Install Text2Podcast")

def install(installpath, tesspath, ffmpath):
    pass



#Main Install GUI
def GUI():
    global main

    #How to Label
    Label(main, text="Welcome! This is an Installer which will install Text2Podcast on your PC").pack()
    Label(main, text="First install Google Tesseract and FFMPEG on your Computer then copy the paths into the designated Textboxes.").pack()
    Label(main, text="Then type in your desired Install path in the designated Textbox").pack()
    Label(main, text="A detailed installation Tutorial for Windows and Linux can be found at https://sites.google.com/view/christoferis/code-projects/text2podcast").pack()
    Label(main, text="FFMPEG Download: http://ffmpeg.org/download.html, Tesseract: https://tesseract-ocr.github.io/tessdoc/Installation.html ").pack()
    
    #Inputs
    #Tesseract Path
    Label(main, text="\nPath to Tesseract Binaries").pack()
    tesspath = Entry(main)
    tesspath.insert(index=0, string="C:\Program Files\Tesseract-OCR")
    tesspath.pack(fill="x")

    #FFMPEG Path
    Label(main, text="\nPath to FFMPEG Binaries").pack()
    ffmpath = Entry(main)
    ffmpath.insert(index=0, string="C:\Program Files\FFMPEG")
    ffmpath.pack(fill="x")

    #installation path
    Label(main, text="\nInstallpath").pack()
    installpath = Entry(main)
    installpath.insert(index=0, string=r"C:\Users\Public\documents\Christoferis\Text2Podcast")
    installpath.pack(fill="x")

    #start Button
    Button(main, text="Install now", foreground="white", background="green").pack(pady=11)

#instance
GUI()

#mainloop
main.mainloop()