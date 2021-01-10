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

from tkinter import Tk, Label, Entry, Button, Frame, Toplevel
from tkinter.filedialog import askdirectory as diropen
from os import mkdir, system
from json import dump
from shutil import copy

#Instance window
main = Tk()
main.title("Install Text2Podcast")

def install(installpath, tesspath, ffmpath):
    global main

    #install dependencies
    system("pip install -r installer/bin/requirements.txt")

    #create filestructure
    filestruct(installpath)

    #create Binary files
    createbin(installpath, tesspath, ffmpath)


    #make success message
    fin = Toplevel(main)
    Label(fin, text="Text2Podcast is now installed!").pack()
    Button(fin, text="Ok", command=main.destroy).pack()



def filestruct(installpath):
    #make temp directory
    try:
        mkdir(installpath+ "/temp")
    except FileExistsError:
        pass

    #make fin directory
    try:
        mkdir(installpath + "/fin")
    except FileExistsError:
        pass


def createbin(installpath, tesspath, ffmpath):
    global main
    #create paths.json in source directory and append paths to it
    storeobj = {
        "tesseract": tesspath,
        "ffmpeg": ffmpath
        }
    try:
        pathdata = open(installpath + "/paths.json", "w")
        dump(obj=storeobj, fp=pathdata)
        pathdata.close()
    except Exception as e:
        ex = Toplevel(main)
        Label(ex, text=e).pack()


    #Copy data from installer bin
    try:
    #main GUI Script
        copy(src="installer/bin/GUI.pyw", dst=installpath + "/GUI.pyw")
        #Midend
        copy(src="installer/bin/Midend.pyw", dst=installpath + "/Midend.pyw")
        #Backend
        copy(src="installer/bin/Backend.pyw", dst=installpath + "/Backend.pyw")
    except Exception as e:
        ex = Toplevel(main)
        Label(ex, text=e).pack()


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
    tesspath.insert(index=0, string="C:/Program Files/Tesseract-OCR/tesseract.exe")
    tesspath.pack(fill="x")

    #FFMPEG Path
    Label(main, text="\nPath to FFMPEG Binaries").pack()
    ffmpath = Entry(main)
    ffmpath.insert(index=0, string="C:/Program Files/ffmpeg-N-99728-gd6e903b09b-win64-gpl-shared-vulkan/ffmpeg-N-99728-gd6e903b09b-win64-gpl-shared-vulkan/bin/ffmpeg.exe")
    ffmpath.pack(fill="x")

    #installation path
    Label(main, text="\nInstallpath").pack()
    installpath = Entry(main)
    installpath.insert(index=0, string=r"C:\Users\Public\documents\Christoferis\Text2Podcast")
    installpath.pack(fill="x")

    #start Button
    Button(main, text="Install now", foreground="white", background="green", command=lambda: install(installpath.get(), tesspath.get(), ffmpath.get())).pack(pady=11)
    Button(main, text="Cancel", foreground="black", background="white", command=main.destroy).pack(pady=11)

#instance
GUI()

#mainloop
main.mainloop()