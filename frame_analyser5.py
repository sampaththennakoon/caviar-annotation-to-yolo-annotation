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
file = minidom.parse(input_base_dir + input_caviar_browse6_file_path)

#use getElementsByTagName() to get tag
frames = file.getElementsByTagName('frame')
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


# movement_set:  {'active', 'walking', 'inactive'}
# role_set:  {'walker', 'browser'}
# context_set:  {'browsing', 'walking', 'immobile'}
# situation_set:  {'moving', 'browsing', 'inactive'}

# movement_set:  {'active'}
# role_set:  {'browser'}
# context_set:  {'browsing'}
# situation_set:  {'browsing'}

# movement_set:  {'walking', 'active'}
# role_set:  {'browser', 'walker'}
# context_set:  {'walking', 'browsing'}
# situation_set:  {'moving', 'browsing'}

# movement_set:  {'inactive', 'active'}
# role_set:  {'browser'}
# context_set:  {'browsing'}
# situation_set:  {'browsing'}

# movement_set:  {'walking', 'active'}
# role_set:  {'browser', 'walker'}
# context_set:  {'browsing', 'immobile'}
# situation_set:  {'browsing', 'moving'}

# movement_set:  {'inactive'}
# role_set:  {'browser'}
# context_set:  {'browsing'}
# situation_set:  {'browsing'}

