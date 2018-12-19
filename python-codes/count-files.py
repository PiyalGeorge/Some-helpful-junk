'''
This code is to count the files in a directory/folder
'''

import os

directory = "/home/vkchcp0013/Documents/Helpful-codes" # Enter directory 

number_files = len(os.listdir(directory)) 
print("The total number of files:", number_files)

