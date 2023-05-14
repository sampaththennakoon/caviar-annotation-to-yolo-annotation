from xml.dom import minidom
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_fighting_chase_jpg_dir = "Fighting/Fight_Chase/JPEGS/"
input_caviar_fighting_one_man_down_jpg_dir = "Fighting/Fight_OneManDown/JPEGS/"
input_caviar_fighting_fight_run_away1_jpg_dir = "Fighting/Fight_RunAway1/JPEGS/"
input_caviar_fighting_fight_run_away2_jpg_dir = "Fighting/Fight_RunAway2/JPEGS/"
input_caviar_fighting_chase_annotation_file_path = "Fighting/Fight_Chase/fcgt11.xml"
input_caviar_fighting_one_man_down_annotation_file_path1 = "Fighting/Fight_OneManDown/fomdgt11.xml"
input_caviar_fighting_one_man_down_annotation_file_path2 = "Fighting/Fight_OneManDown/fomdgt22.xml"
input_caviar_fighting_one_man_down_annotation_file_path3 = "Fighting/Fight_OneManDown/fomdgt33.xml"
input_caviar_fighting_fight_run_away1_annotation_file_path = "Fighting/Fight_RunAway1/fra1gt11.xml"
input_caviar_fighting_fight_run_away2_annotation_file_path = "Fighting/Fight_RunAway2/fra2gt11.xml"

# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_fighting_chase_annotation_file_path)

#use getElementsByTagName() to get tag
frames = file.getElementsByTagName('frame')
count = 0
count = 0
movement_list = []
role_list = []
context_list = []
situation_list = []

for frame in frames:
    movements = frame.getElementsByTagName("movement")
    for movement in movements:
        movement_list.append(movement.firstChild.data)

for frame in frames:
    roles = frame.getElementsByTagName("role")
    for role in roles:
        role_list.append(role.firstChild.data)

for frame in frames:
    contexts = frame.getElementsByTagName("context")
    for context in contexts:
        context_list.append(context.firstChild.data)

for frame in frames:
    situations = frame.getElementsByTagName("situation")
    for situation in situations:
        situation_list.append(situation.firstChild.data)

movement_set = set(movement_list)
role_set = set(role_list)
context_set = set(context_list)
situation_set = set(situation_list)

print('movement_set: ', movement_set)
print('role_set: ', role_set)
print('context_set: ', context_set)
print('situation_set: ', situation_set)



# movement_set:  {'active', 'running', 'inactive', 'walking', 'movement'}
# role_set:  {'walker', 'fighter', 'fighters'}
# context_set:  {'fighting', 'immobile', 'walking'}
# situation_set:  {'split up', 'fighting', 'moving', 'joining', 'inactive'}

# movement_set:  {'running', 'movement', 'walking', 'inactive', 'active'}
# role_set:  {'fighters', 'walker'}
# context_set:  {'fighting', 'walking', 'drop down', 'immobile'}
# situation_set:  {'moving', 'leaving victim', 'fighting', 'inactive', 'joining'}

# movement_set:  {'inactive', 'walking', 'active', 'running', 'movement'}
# role_set:  {'browser', 'meeters', 'leaving group', 'walker', 'fighter', 'leaving victim', 'fighters'}
# context_set:  {'drop down', 'browsing', 'walking', 'fighting', 'immobile', 'meeting'}
# situation_set:  {'split up', 'inactive', 'browsing', 'interacting', 'fighting', 'moving', 'leaving victim', 'joining'}

# movement_set:  {'walking', 'running', 'active', 'inactive', 'movement'}
# role_set:  {'walker', 'browser', 'fighters'}
# context_set:  {'drop down', 'walking', 'fighting', 'browsing'}
# situation_set:  {'inactive', 'fighting', 'browsing', 'moving', 'split up', 'joining'}

# movement_set:  {'running', 'active', 'movement', 'inactive', 'walking'}
# role_set:  {'fighters', 'walker'}
# context_set:  {'walking', 'fighting', 'immobile'}
# situation_set:  {'moving', 'fighting', 'joining', 'split up', 'inactive'}

# movement_set:  {'running', 'active', 'walking', 'movement', 'inactive'}
# role_set:  {'fighters', 'walker'}
# context_set:  {'fighting', 'immobile', 'walking'}
# situation_set:  {'fighting', 'split up', 'joining', 'moving', 'inactive'}

