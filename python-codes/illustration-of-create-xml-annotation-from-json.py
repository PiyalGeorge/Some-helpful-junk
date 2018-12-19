'''

'''

import os
import json
from PIL import Image


required_labels = ["bike", "bus", "car", "motor", "person"]

def load_annotations(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
        for count, item in enumerate(data):
            image_id= item['name']
            filename = os.path.splitext(image_id)[0]
            labels = item['labels']
            source_train = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/downloads/vehicle-dataset/Images/100k/train/"+image_id
            source_test = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/downloads/vehicle-dataset/Images/100k/test/"+image_id
            source_val = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/downloads/vehicle-dataset/Images/100k/val/"+image_id
            
            if os.path.isfile(source_train):
                new_label_file = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/downloads/vehicle-dataset/labels/train/{}.xml".format(filename)
                source = source_train
            elif os.path.isfile(source_test):
                new_label_file = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/downloads/vehicle-dataset/labels/test/{}.xml".format(filename)
                source = source_test
            elif os.path.isfile(source_val):
                new_label_file = "/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/downloads/vehicle-dataset/labels/val/{}.xml".format(filename)
                source = source_val
            else:
                source = source_train

            if os.path.isfile(source):                
                img = Image.open(source)
                width, height = img.size
                third_post =[]
            
                for each_label in labels:
                    if each_label['category'] in required_labels:
                        classname = each_label['category']
                        confidence = 1
                        xmin = int(float(each_label['box2d']['x1']))
                        xmax = int(float(each_label['box2d']['x2']))
                        ymin = int(float(each_label['box2d']['y1']))
                        ymax = int(float(each_label['box2d']['y2']))
                        
                        truncated = 1 if str(each_label['attributes']['truncated'])=='true' else 0

                        third_pre = "\n  \
      <object>\n  \
              <name>{}</name>\n  \
              <pose>Unspecified</pose>\n  \
              <truncated>{}</truncated>\n  \
              <difficult>0</difficult>\n  \
              <bndbox>\n  \
                      <xmin>{}</xmin>\n  \
                      <ymin>{}</ymin>\n  \
                      <xmax>{}</xmax>\n  \
                      <ymax>{}</ymax>\n  \
              </bndbox>\n  \
      </object>".format(classname, truncated, xmin, ymin, xmax, ymax)

                        third_post.append(third_pre)
                third_final = third_post

                first = "<annotation>\n  \
      <folder>COCO</folder>\n  \
      <filename>{}</filename>\n  \
      <source>\n  \
              <database>The VOC2007 Database</database>\n  \
              <annotation>PASCAL VOC2007</annotation>\n  \
              <image>flickr</image>\n  \
      </source>".format(image_id)

                second = "\n  \
      <size>\n  \
              <width>{}</width>\n  \
              <height>{}</height>\n  \
              <depth>3</depth>\n  \
      </size>\n  \
      <segmented>1</segmented>".format(width, height)

                if len(third_final)>0:
                    third = third_final[0]
            
                    for para in range(1,len(third_final)):
                        third = third + third_final[para]

                    last = "\n</annotation>"

                    final = first+second+third+last
                    file = open(new_label_file, "w")
                    file.write(final) 
                    file.close()
            
            print(count)
        return True

#Format be like:- [{imageid:[{classid ,xmin, ymin, xmax, ymax, confidence}]}, {imageid:[{classid ,xmin, ymin, xmax, ymax, confidence}]}]
    
annotation_detail = load_annotations("/media/vkchcp0013/mstu_hpat/ZFGG_PRSC/new-dataset/downloads/labels/bdd100k_labels_images_train.json")

print("Got all Annotations")
if annotation_detail is True:
    print("Its Finished")


'''
The eg output xml file looks like this:
'''

# 0a0c1f65f19859c0.xml
"""
<annotation>
   	<folder>COCO</folder>
  	<filename>0a0c1f65f19859c0.jpeg</filename>
  	<source>
  		<database>The VOC2007 Database</database>
  		<annotation>PASCAL VOC2007</annotation>
  		<image>flickr</image>
  	</source>
  	<size>
  		<width>512</width>
  		<height>512</height>
  		<depth>3</depth>
  	</size>
  	<segmented>1</segmented>
  	<object>
  		<name>face</name>
  		<pose>Unspecified</pose>
  		<truncated>0</truncated>
  		<difficult>0</difficult>
  		<bndbox>
  			<xmin>216</xmin>
  			<ymin>0</ymin>
  			<xmax>278</xmax>
  			<ymax>64</ymax>
  		</bndbox>
  	</object>
  	<object>
  		<name>face</name>
  		<pose>Unspecified</pose>
  		<truncated>0</truncated>
  		<difficult>0</difficult>
  		<bndbox>
  			<xmin>153</xmin>
  			<ymin>72</ymin>
  			<xmax>192</xmax>
  			<ymax>131</ymax>
  		</bndbox>
  	</object>
  	<object>
  		<name>person</name>
  		<pose>Unspecified</pose>
  		<truncated>0</truncated>
  		<difficult>0</difficult>
  		<bndbox>
  			<xmin>210</xmin>
  			<ymin>0</ymin>
  			<xmax>434</xmax>
  			<ymax>512</ymax>
  		</bndbox>
  	</object>
</annotation>
"""



