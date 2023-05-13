from xml.dom import minidom
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_browse1_file_path = "Browsing/Browse1/br1gt1.xml"
input_caviar_browse2_file_path = "Browsing/Browse2/br2gt1.xml"
input_caviar_browse3_file_path = "Browsing/Browse3/br3gt1.xml"
input_caviar_browse4_file_path = "Browsing/Browse4/br4gt1.xml"
input_caviar_browse5_file_path = "Browsing/Browse_WhileWaiting1/bww1gt1.xml"
input_caviar_browse6_file_path = "Browsing/Browse_WhileWaiting2/bww2gt1.xml"

# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_browse1_file_path)

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





