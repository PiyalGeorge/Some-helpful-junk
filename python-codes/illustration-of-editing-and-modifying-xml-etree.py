'''
This code is used to edit and modify the xml files using Element-tree
'''

import os
import xml.etree.ElementTree

src = '/media/Image-data/Image-dataset/wanted/copy/bicycle/bicycle-labels'
fileList = os.listdir(src)

for count, eachfile in enumerate(fileList):
    print("files executed:", count)
    element = xml.etree.ElementTree.parse(src+'/'+eachfile)
    root = element.getroot()
    all_obj =root.findall('object')
    for i in range(len(all_obj)):
        obj_label = all_obj[i][0].text
        if obj_label == "Truck":
            all_obj[i][0].text = "truck"
        elif obj_label == "Car":
            all_obj[i][0].text = "car"
        else:
            pass
     
    element.write('/media/Image-data/Image-dataset/wanted/copy/bicycle/refined-bicycle-labels/'+eachfile)

