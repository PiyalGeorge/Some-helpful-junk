'''
This code is to convert video to images
'''

import cv2

vs = cv2.VideoCapture("/media/my_video-7.mkv") # Enter the video here
image_result = '/media/images' # Enter the result image location here

file_count = 1

while(vs.isOpened()):
    ret, frame = vs.read()
    if ret == True:
        image = frame.copy()
	file_name = str(file_count).zfill(4) # So that file name will be appended by 0, making total string size 4
	cv2.imshow("Output", image)
        cv2.imwrite(image_result+'/{}.jpg'.format(file_name), image)
        cv2.waitKey(1)
        file_count = file_count+1
    else:
	break







