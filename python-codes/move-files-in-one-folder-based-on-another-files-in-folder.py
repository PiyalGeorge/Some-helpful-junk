'''
This code is used to move files in one folder based on the files in another folder
Eg situation: move images in one folder based on xml files in another folder
'''

import shutil
import os

def move_over(src_dir, dest_dir):
    fileList = os.listdir(src_dir)
    src_img_dir = '/home/data/ssd-own-data-original/kitti-ssd/MyDataset/new-created/open-images-car-bus-motorcycle-bicycle-truck-zip/Images'  # Source of images
    dest_img_dir = '/media/new-dataset/open-images-2000-each/2000-set/2000-truck-images' # Destination of images
    counter = 0
    for count, i in enumerate(fileList):
        print("files executed:", count)
        name_only = os.path.splitext(i)[0]+'.jpg'
        check = os.path.join(src_img_dir, name_only)
        if os.path.isfile(check):
#             src = os.path.join(src_dir, i)
#             dest = os.path.join(dest_dir, i)
#             shutil.move(src, dest_dir)
            shutil.move(check, dest_img_dir)
#             shutil.copy(check, dest_img_dir)
            counter = counter+1

dest_dir = '/home/data/ssd-own-data-original/kitti-ssd/MyDataset/new-created/small-and-big-images-copy/exact-labels' # Destination of xml files(not necessary, all the time)
src_dir = '/media/new-dataset/open-images-2000-each/2000-set/2000-truck'  # Source of xml files

move_over(src_dir, dest_dir)




