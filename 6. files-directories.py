import os
import glob

"""
The current working directory
"""
print(os.getcwd())      # get the current working directory
os.chdir('D:\\Python\\files')    # change the current working directory
print(os.getcwd())      # will print D:\Python\files
print(os.stat('ex1.txt'))       # stat returns an object that contains some metadata about the given file

"""
Filenames and Directory names
path - contains functions for manipulating filenames and directory names
"""
print(os.path.join('D:\\Python\\files\\', 'example.txt'))        # print D:\Python\files\example.txt

"""
listing files in a directory
"""
print (glob.glob('*.txt'))      # print a list which contains name of all txt files from working directory
