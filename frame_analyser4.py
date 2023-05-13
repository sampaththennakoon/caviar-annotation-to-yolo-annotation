from xml.dom import minidom
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_meeting1_file_path = "Meeting/Meet_Crowd/mc1gt1.xml"
input_caviar_meeting2_file_path = "Meeting/Meet_Split_3rdGuy/ms3ggt1.xml"
input_caviar_meeting3_file_path = "Meeting/Meet_WalkSplit/mws1gt1.xml"
input_caviar_meeting4_file_path = "Meeting/Meet_WalkTogether1/mwt1gt1.xml"
input_caviar_meeting5_file_path = "Meeting/Meet_WalkTogether2/mwt2gt1.xml"
input_caviar_meeting6_file_path = "Meeting/Split/spgt1.xml"

# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_meeting6_file_path)

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





