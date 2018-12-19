'''
This code is used to perform object-detection in video and return a video output with detections. The object detection is done with caffe's model and deploy file and with cv2's DNN moodule. 
'''

import os
import cv2
import numpy as np


CLASSES = ["background", "car", "bus", "motorcycle" , "bicycle", "truck"] # Modify the class labels if necessary

prototxt = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/siva/object-detection-deep-learning/models/open-images-6-classes/MobileNetSSD_deploy.prototxt.txt" # Enter the prototxt ending with .txt format
model = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/siva/object-detection-deep-learning/models/open-images-6-classes/MobileNetSSD_deploy.caffemodel" # Enter the caffemodel

print("[INFO] loading model...")
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))
net = cv2.dnn.readNetFromCaffe(prototxt, model)

vs = cv2.VideoCapture("/home/vkchcp0013/Documents/Helpful-codes/video.avi") # Upload the video input here

while(vs.isOpened()):
  	ret, frame = vs.read()
        height , width , layers =  frame.shape
        #fourcc = cv2.cv.CV_FOURCC(*'XVID') # Incase of error replace with this - cv2.VideoWriter_fourcc(*'XVID')
        try:
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
        except:
            fourcc = cv2.cv.CV_FOURCC(*'XVID')

        fps=30
        size = (width, height)
        is_color=True
        cwd = os.getcwd()
        output_video = cwd+'/video.avi' # Saves the resulting detection video in current directory 
        video = cv2.VideoWriter(output_video, fourcc, float(fps), size, is_color)
	break;

if (vs.isOpened()== False): 
  print("Error opening video stream or file")

while(vs.isOpened()):
  	ret, frame = vs.read()
  	if ret == True:
		image = frame.copy()
		#image = cv2.imread('/home/vkchcp0013/data/ssd-own-data-original/kitti-ssd/MyDataset/new-created/Images/10.jpg') # Input the image input here if testing with single image 
		(h, w) = image.shape[:2]
		blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

		print("[INFO] computing object detections...")
		net.setInput(blob)
		detections = net.forward()

		for i in np.arange(0, detections.shape[2]):
			confidence = detections[0, 0, i, 2]
			if confidence > 0.5: # .6 is the minimum confidence, modify this if necessary
				idx = int(detections[0, 0, i, 1])
				box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
				(startX, startY, endX, endY) = box.astype("int")
				label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
				print("[INFO] {}".format(label))
				cv2.rectangle(image, (startX, startY), (endX, endY), (255, 255, 255), 2)# COLORS[idx], 2) # For white color of rectangle
				y = startY - 15 if startY - 15 > 15 else startY + 15
				cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2) #COLORS[idx], 2) # For white color of box

		cv2.imshow("Output", image)
                cv2.imwrite(cwd+'/.frame.jpg',image) # Hidden image is saved
                img = cv2.imread(cwd+'/.frame.jpg') # Hidden image is read
                video.write(img)

		key = cv2.waitKey(20)
                if key == 27: # exit on ESC
                    break
		cv2.waitKey(1)
	else:
		break

vs.release()
cv2.destroyAllWindows()	





