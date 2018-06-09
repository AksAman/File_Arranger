import argparse
import os


# Setting up the argument parsing
parser = argparse.ArgumentParser(
    description='This program helps to rearrange files in a folder, and move them into new folders named as their filetypes')
parser.add_argument(
    'path', help='The path, where you want to arrange your files [write the path in \'\'] and end with \\')
args = parser.parse_args()
path=args.path
print(path)

# changing to specified path
try:
	os.chdir(path)
except FileNotFoundError:
	print('Path provided doesn\'t exist')


fileTypedict={}
files=os.listdir()
for file in files:
	if (not os.path.isdir(file)):
		if(not file.find('.') is -1):
			extension=file.split('.')[-1]
			fileTypedict[extension]=''

print(fileTypedict)



