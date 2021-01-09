#Update main files in installer binary section
#Imports
from shutil import copy


def update():
    copy(src="GUI.py", dst="installer/installer_bin/GUI.pyw")
    copy(src="Midend.py", dst="installer/installer_bin/Midend.pyw")
    copy(src="Backend.py", dst="installer/installer_bin/Backend.pyw")
    

update()