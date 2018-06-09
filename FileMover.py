import argparse
import os


# Setting up the argument parsing
parser = argparse.ArgumentParser(
    description='This program helps to rearrange files in a folder, and move them into new folders named as their filetypes')
parser.add_argument(
    'path', help='The path, where you want to arrange your files')
args = parser.parse_args()
