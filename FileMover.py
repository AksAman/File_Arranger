import argparse
import os


# Setting up the argument parsing
parser = argparse.ArgumentParser(
    description='This program helps to rearrange files in a folder, and move them into new folders named as their filetypes')
parser.add_argument(
    'path', help='The path, where you want to arrange your files [write the path in \'\'] and end with \\')
args = parser.parse_args()
path = args.path

# changing to specified path
try:
    os.chdir(path)
except FileNotFoundError:
    print('Path provided doesn\'t exist')

# This dictionary will store all the file extensions in th path
# and, those extensions refer to list containing files with that extension
fileTypedict = {}

# List to store all the files
files = []

# os.listdir() returns all the files in the current working directory as a list
"""
 Bug to be removed : if the file is named as 'This.is.a.file', then it will be counted
 too with 'file' as extension.
"""
for f in os.listdir():
    # Checking if the current file is not a directory if the current file has an extensions or not
    if (not os.path.isdir(f) and not f.find('.') is -1):
        files.append(f)


# Populating the file type dictionary with extension and assigning empty list to
# ...each extension
for file in files:
    extension = file.split('.')[-1].lower()
    fileTypedict[extension] = []

# Appending files with file extension in dict to the empty list assigned to them
for ext in fileTypedict:
    for file in files:
        curExt = file.split('.')[-1].lower()
        if(curExt == ext):
            fileTypedict[ext].append(file)


for ext in fileTypedict:
    try:
        # Making empty directory as per extension
        os.mkdir(ext)
    except Exception as e:
        print(e)


# Finally running system command for move
for ext in fileTypedict:
    for file in fileTypedict[ext]:
        command = 'move "' + file + '" ' + '"' + ext + '"'
        os.system(command)
