from xml.dom import minidom
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_fighting_chase_jpg_dir = "Fighting/Fight_Chase/JPEGS/"
input_caviar_fighting_one_man_down_jpg_dir = "Fighting/Fight_OneManDown/JPEGS/"
input_caviar_fighting_fight_run_away1_jpg_dir = "Fighting/Fight_RunAway1/JPEGS/"
input_caviar_fighting_fight_run_away2_jpg_dir = "Fighting/Fight_RunAway2/JPEGS/"
input_caviar_fighting_chase_annotation_file_path = "Fighting/Fight_Chase/fcgt1.xml"
input_caviar_fighting_one_man_down_annotation_file_path1 = "Fighting/Fight_OneManDown/fomdgt11.xml"
input_caviar_fighting_one_man_down_annotation_file_path2 = "Fighting/Fight_OneManDown/fomdgt22.xml"
input_caviar_fighting_one_man_down_annotation_file_path3 = "Fighting/Fight_OneManDown/fomdgt33.xml"
input_caviar_fighting_fight_run_away1_annotation_file_path = "Fighting/Fight_RunAway1/fra1gt1.xml"
input_caviar_fighting_fight_run_away2_annotation_file_path = "Fighting/Fight_RunAway2/fra2gt1.xml"

# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_fighting_fight_run_away2_annotation_file_path)

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





