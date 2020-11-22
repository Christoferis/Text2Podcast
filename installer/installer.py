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

from os import startfile, system, mkdir
from time import sleep




#main Install function
def yesno(msg):
    #loop over until final answer
    while True:
        yn =  input(msg + "(y/n)?: ")

        if yn in ("y", "Y"):
            break
        #no
        elif yn in ("n", "N"):
            print("Closing in 10 seconds")
            sleep(10)
            exit()
        #different
        else:
            print("y/n please")
            pass

    return bool(True)



def directory(path):
    #make main dir
    mkdir(path, "\Christoferis")
    mainpath = path + "\Christoferis"

    #make temp path
    mkdir(path)
    pass



def start():
    print("Welcome to the Text2Podcast Installer by Christoferis")
    print("This installs the Text2Podcast to your Computer \n")
    print("To start the installation, please install the following Software first (Follow Installation Details on Github or the respective Software Pages): ")
    print("FFMPEG: http://ffmpeg.org/download.html")
    print("Google Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki\n")
    print("Locate the Install location of the installed software and add them to the 'PATH' Variable")
    
    if yesno("Type 'y' if you're finished installing and to proceed installing"):
        print("License Agreement (CC BY-SA 4.0) \n" + LICENSE)
        installpath = 'C:\Users\Public\Documents'

        if yesno("Agree License Agreement? : "):
            install = input("\n Where should Text2Podcast be installed? (CURRENT: " + installpath + " ) enter 0 to install to default path: ")

            #Default Path thingy
            if install != 0:
                installpath = install
                directory(installpath)




        
#main Buffer
start()
