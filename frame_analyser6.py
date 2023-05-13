from xml.dom import minidom
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_leaving1_file_path = "Leaving/LeftBag/lb1gt1.xml"
input_caviar_leaving2_file_path = "Leaving/LeftBag_AtChair/lb2gt1.xml"
input_caviar_leaving3_file_path = "Leaving/LeftBag_BehindChair/lbbcgt1.xml"
input_caviar_leaving4_file_path = "Leaving/LeftBag_PickedUp/lbpugt1.xml"
input_caviar_leaving5_file_path = "Leaving/LeftBox/lbgt1.xml"
# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_leaving5_file_path)

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





