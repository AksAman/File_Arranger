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
files=[]

for f in os.listdir():
	if (not os.path.isdir(f)):
		if(not f.find('.') is -1):
			files.append(f)

for file in files:
	extension=file.split('.')[-1].lower()
	fileTypedict[extension]=[]

for ext in fileTypedict:
	for file in files:
		curExt=file.split('.')[-1].lower()
		if(curExt == ext):
			fileTypedict[ext].append(file)

# print('after append')
# print(fileTypedict)

for ext in fileTypedict:
	try:
		os.mkdir(ext)
	except Exception:
		print(Exception)


for ext in fileTypedict:
	for file in fileTypedict[ext]:
		command='move "'+file+'" '+'"'+ext+'"'
		print(command)
		os.system(command)