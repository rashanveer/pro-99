import os
import shutil

source = input("source")
source = source+"/"
destination = input("enter your destination:")
destination = destination+"/"
listOffiles = os.listdir(source)
for file in listOffiles:
    #shutil.copy(source+file,destination)
    shutil.move(source+file,destination)