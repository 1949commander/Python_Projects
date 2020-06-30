import glob
import os
import datetime
import shutil
# Find files
originPath = ('C:/Users/breev/OneDrive/Desktop/Folder_A')
destinationPath = ('C:/Users/breev/OneDrive/Desktop/Folder_B')
fileType = ".txt"

def get_file_list(self):
    self.originPath = originPath
    self.type = fileType
    self.destinationPath = destinationPath
    '''
    Return a list of filename matching the given path and file type
    '''
    return(glob.glob(self.originPath + "*" + self.type))



print('{} {}'.format(originPath, type))
# Create list of text filenames in Origin folder

fileList = get_file_list()
print(fileList)

for self.file in self.fileList:
# Get last modified date and today's date
    modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    todaysDate = datetime.datetime.today()

filePathList = file.split("\\") # Create a list from the filepath
filename = filePathList[-1] # The last element is a the filename

# If modified within last 24 hours, then copy to destination folder
modifyDateLimit = modifyDate + datetime.timedelta(days=1)

# If the file was edited less then 24 hours ago then copy it
if modifyDateLimit > todaysDate:
    shutil.copy2(file, self.destinationPath + filename)    


    

