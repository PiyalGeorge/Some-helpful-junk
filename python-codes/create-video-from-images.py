'''
This code is to create video from images
'''

import os
import cv2

try:
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
except:
    fourcc = cv2.cv.CV_FOURCC(*'XVID')

#fourcc = cv2.VideoWriter_fourcc(*'mp4v') better apply this if video result is .mp4, else warning will be shown at begining of execution

fps=30
size=(960, 480)  # Adjust this according to your width and height of the image
is_color=True

result_dir = '/home/vkchcp0013/Videos/wow' # Video location folder

output_video = result_dir+'/output-video.avi'

video = cv2.VideoWriter(output_video, fourcc, float(fps), size, is_color)

src = '/home/vkchcp0013/data/ssd-own-data-original/kitti-ssd/MyDataset/new-created/just-new/siva-yesterday/video/images' # Image location folder

list_img = os.listdir(src)

for count, each_file in enumerate(sorted(list_img)):
    print("Images processed:", count)
    img = cv2.imread(src+'/'+each_file)
    video.write(img)    


