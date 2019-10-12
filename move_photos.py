import os

# photo file extensions
photo_file = list(['.jpg', '.jpeg', '.png', '.TIFF', '.RAW', '.JPEG', '.JPG', '.PNG'])
x = 0 # file counterff

# whitelist for directoriess
fileDirList = list(['Downloads', 'Documents', 'Photos', 'Pictures', 'Documents'])

# change directory to root
os.chdir('/')
os.chdir('Users')
os.chdir('sleezyk1d')

# get current working directory
current_dir = os.getcwd()

# grab all folders in current directory
filenames= os.listdir (".")
result = []
for filename in filenames:  # loop through all the files and folders
    if os.path.isdir(
            os.path.join(os.path.abspath("."), filename)):  # check whether the current object is a folder or not
        result.append(filename)

result.sort()
for folder in result:
    if folder in fileDirList:
        os.chdir(current_dir + "\\" + folder)
        for roots, dirs, files in os.walk(os.getcwd()):
            # Count all files
            for file in files:
                for file_type in photo_file:
                    if file[-4:] == file_type:
                        # move file
                        path_with_file = os.path.join(roots, file)
                        x += 1
                        print("Moved " + path_with_file + "! Total: " + str(x))