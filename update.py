#Update main files in installer binary section
#Imports
from shutil import copy


def update():
    try:
        copy(src="GUI.py", dst="installer/installer_bin/GUI.pyw")
        copy(src="Midend.py", dst="installer/installer_bin/Midend.pyw")
        copy(src="Backend.py", dst="installer/installer_bin/Backend.pyw")
        print("Done.")
    except Exception as ex:
        print(ex)
    

update()