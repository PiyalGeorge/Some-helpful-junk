'''
This code is an example of reading csv file as dict. Advantage of reading it as a dict is it returns the csv value as dict, with key value pair, where key is the each heading in first line of csv file. However, The best method to read large csv file is using pandas.
This code is just an example.
'''

import os
import csv

required_labels = [ "/m/03ldnb", "/m/03m3pdh", "/m/03ssj5"]

def load_annotations(filepath):
    annotations = []    
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for item in reader:
            if item['LabelName'] in required_labels:
                annotation = {
                    'image_id': item['ImageID'],
                    'class_id': item['LabelName'],
                    'confidence': item['Confidence'],
                    'xmin': item['XMin'],
                    'xmax': item['XMax'],
                    'ymin': item['YMin'],
                    'ymax': item['YMax'],
                }
                annotations.append(annotation)
    return annotations

annotation_detail = load_annotations("/media/Image-data/validation/validation-annotations-bbox.csv")

print("Size of annotations",len(annotation_detail))


