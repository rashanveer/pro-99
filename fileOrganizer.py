import os
import shutil

path  = "nd"
listOffiles = os.listdir(path)
for file in listOffiles:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+file,path+"/"+ext+"/"+file)
