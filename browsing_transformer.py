from xml.dom import minidom
import os

image_width = 384
image_height = 288

# classes definition
classes = dict()
classes['walking'] = 0
classes['immobile'] = 1
classes['meeting'] = 2
classes['browsing'] = 3
classes['fighting'] = 4
classes['drop down'] = 5
classes['leaving'] = 6

input_base_dir = "caviar_annotations/"
input_caviar_browse1_file_path = "Browsing/Browse1/br1gt1.xml"
input_caviar_browse2_file_path = "Browsing/Browse2/br2gt1.xml"
input_caviar_browse3_file_path = "Browsing/Browse3/br3gt1.xml"
input_caviar_browse4_file_path = "Browsing/Browse4/br4gt1.xml"
input_caviar_browse5_file_path = "Browsing/Browse_WhileWaiting1/bww1gt1.xml"
input_caviar_browse6_file_path = "Browsing/Browse_WhileWaiting2/bww2gt1.xml"
output_dir = "/home/samx/Documents/PROJECTS/caviar-annotation-to-yolo-annotation/output"

def safe_division(x, y):
    if y == 0:
        return 0
    return round(x / y, 4)

file_list = []
file_list.append(input_caviar_browse1_file_path)
# file_list.append(input_caviar_browse2_file_path)
# file_list.append(input_caviar_browse3_file_path)
# file_list.append(input_caviar_browse4_file_path)
# file_list.append(input_caviar_browse5_file_path)
# file_list.append(input_caviar_browse6_file_path)

for file_path in file_list:
    # parse an xml file by name
    xml_file_path = minidom.parse(input_base_dir + file_path)

    # use getElementsByTagName() to get tag
    frames = xml_file_path.getElementsByTagName('frame')
    for frame in frames:

        # Initialize the YOLO TXT
        filename = frame.getAttribute('number')
        result = []
        bbox_string = ""
        object_numbers = []
        group_one = None

        # analyse group list
        if len(frame.getElementsByTagName("group")) > 0:
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
                movement = hypothesis_one.getElementsByTagName("movement")[0].firstChild.data
                role = hypothesis_one.getElementsByTagName("role")[0].firstChild.data
                context = hypothesis_one.getElementsByTagName("context")[0].firstChild.data
                situation = hypothesis_one.getElementsByTagName("situation")[0].firstChild.data

                if context == 'browsing' and (movement == 'active' or movement == 'inactive'):
                    index = classes[context]
                elif context == 'browsing' and movement == 'walking' and situation == 'moving':
                    index = classes['walking']
                else:
                    index = classes[context]

                result.append(f"{index} {bbox_string}")

        if group_one is not None:
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






