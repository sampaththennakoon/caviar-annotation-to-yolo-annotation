from xml.dom import minidom
import os

# classes definition
classes = dict()
classes['walking'] = 0
classes['immobile'] = 1
classes['meeting'] = 2
classes['browsing'] = 3
classes['fighting'] = 4
classes['drop down'] = 5

def getNodeText(node):
    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

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
output_dir = "/home/samx/Documents/PROJECTS/caviar-annotation-to-yolo-annotation/Fight_Chase_Output"

# parse an xml file by name
file = minidom.parse(input_base_dir + input_caviar_fighting_chase_annotation_file_path)

# use getElementsByTagName() to get tag
frames = file.getElementsByTagName('frame')
for frame in frames:

    # Initialize the YOLO TXT
    filename = frame.getAttribute('number')
    result = []
    bbox_string = ""

    # analyse group list
    group_one = frame.getElementsByTagName("group")[0]
    member_one = group_one.getElementsByTagName('members')[0]
    object_numbers = member_one.firstChild.data.split(",")

    # object list
    object_list = frame.getElementsByTagName("object")
    for obj in object_list:
        if obj.getAttribute('id') not in object_numbers:

            yolo_bbox = []
            box_element = obj.getElementsByTagName("box")[0]
            yolo_bbox.append(box_element.getAttribute('xc'))
            yolo_bbox.append(box_element.getAttribute('yc'))
            yolo_bbox.append(box_element.getAttribute('w'))
            yolo_bbox.append(box_element.getAttribute('h'))
            bbox_string = " ".join([str(x) for x in yolo_bbox])

            hypothesis_one = obj.getElementsByTagName("hypothesis")[0]
            index = classes[hypothesis_one.getElementsByTagName("context")[0].firstChild.data]
            result.append(f"{index} {bbox_string}")

    hypothesis_one = group_one.getElementsByTagName('hypothesislist')[0]
    hypothesis_context = hypothesis_one.getElementsByTagName('context')[0].firstChild.data
    group_box = group_one.getElementsByTagName('box')[0]
    yolo_group_bbox = []
    yolo_group_bbox.append(group_box.getAttribute('xc'))
    yolo_group_bbox.append(group_box.getAttribute('yc'))
    yolo_group_bbox.append(group_box.getAttribute('w'))
    yolo_group_bbox.append(group_box.getAttribute('h'))
    bbox_string = " ".join([str(x) for x in yolo_group_bbox])
    index = classes[hypothesis_context]
    result.append(f"{index} {bbox_string}")

    # Write YOLO TXT
    if result:
        # generate a YOLO format text file for each xml file
        with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(result))



