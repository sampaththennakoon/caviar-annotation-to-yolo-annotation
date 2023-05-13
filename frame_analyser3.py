from xml.dom import minidom
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_walk1_file_path = "Walking/Walk1/wk1gt1.xml"
input_caviar_walk2_file_path = "Walking/Walk2/wk2gt2.xml"
input_caviar_walk3_file_path = "Walking/Walk3/wk3gt3.xml"

# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_walk3_file_path)

#use getElementsByTagName() to get tag
frames = file.getElementsByTagName('frame')
count = 0
context_list = []
for frame in frames:
    contexts = frame.getElementsByTagName("context")
    for context in contexts:
        context_list.append(context.firstChild.data)

context_set = set(context_list)
print(context_set)





