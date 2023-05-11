from xml.dom import minidom
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_fighting_chase_jpg_dir = "Fighting/Fight_Chase/JPEGS/"
input_caviar_fighting_one_man_down_jpg_dir = "Fighting/Fight_OneManDown/JPEGS/"
input_caviar_fighting_fight_run_away1_jpg_dir = "Fighting/Fight_RunAway1/JPEGS/"
input_caviar_fighting_fight_run_away2_jpg_dir = "Fighting/Fight_RunAway2/JPEGS/"
input_caviar_fighting_chase_annotation_file_path = "Fighting/Fight_Chase/fcgt1.xml"
input_caviar_fighting_one_man_down_annotation_file_path1 = "Fighting/Fight_OneManDown/fomdgt1.xml"
input_caviar_fighting_one_man_down_annotation_file_path2 = "Fighting/Fight_OneManDown/fomdgt2.xml"
input_caviar_fighting_one_man_down_annotation_file_path3 = "Fighting/Fight_OneManDown/fomdgt3.xml"
input_caviar_fighting_fight_run_away1_annotation_file_path = "Fighting/Fight_RunAway1/fra1gt.xml"
input_caviar_fighting_fight_run_away2_annotation_file_path = "Fighting/Fight_RunAway2/fra2gt.xml"

# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_fighting_chase_annotation_file_path)

#use getElementsByTagName() to get tag
frames = file.getElementsByTagName('frame')
count = 0
for frame in frames:
    groups = frame.getElementsByTagName("group")
    if len(groups) > 2:
        print(len(groups))



