import shutil
import os

#set where the source of the files are
source = '/Users/breev/OneDrive/Desktop/Folder_A/'

#set the destination path to folder_B
destination = '/Users/breev/OneDrive/Desktop/Folder_B/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
