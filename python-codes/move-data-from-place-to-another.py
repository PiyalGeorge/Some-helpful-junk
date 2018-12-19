'''
This file is used to move files from one folder to another
'''

import shutil
import os

def move_over(src_dir, dest_dir):
    fileList = os.listdir(src_dir)
    for count, each in enumerate(fileList):
	print("count:", count)
	#if count<2000: # If you want to give any condition
        src = os.path.join(src_dir, each)
        shutil.move(src, dest_dir)
	#dest = os.path.join(dest_dir, i) # For replace if the file already exist
        #shutil.move(src, dest)


dest_dir = '/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/images/destiny'
src_dir = '/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/images/src'   

move_over(src_dir, dest_dir)

