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
input_caviar_resting1_file_path = "Resting/Rest_FallOnFloor/rffgt1.xml"
input_caviar_resting2_file_path = "Resting/Rest_InChair/ricgt1.xml"
input_caviar_resting3_file_path = "Resting/Rest_SlumpOnFloor/rsfgt1.xml"
input_caviar_resting4_file_path = "Resting/Rest_WiggleOnFloor/rwgt1.xml"
output_dir = "/home/samx/Documents/PROJECTS/caviar-annotation-to-yolo-annotation/output"

file_list = []
file_list.append(input_caviar_resting1_file_path)
file_list.append(input_caviar_resting2_file_path)
file_list.append(input_caviar_resting3_file_path)
file_list.append(input_caviar_resting4_file_path)

def safe_division(x, y):
    if y == 0:
        return 0
    return round(x / y, 4)

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

                xc = safe_division(int(box_element.getAttribute('xc')), image_width)
                yc = safe_division(int(box_element.getAttribute('yc')), image_height)
                w = safe_division(int(box_element.getAttribute('w')), image_width)
                h = safe_division(int(box_element.getAttribute('h')), image_height)

                yolo_bbox.append(xc)
                yolo_bbox.append(yc)
                yolo_bbox.append(w)
                yolo_bbox.append(h)
                bbox_string = " ".join([str(x) for x in yolo_bbox])

                hypothesis_one = obj.getElementsByTagName("hypothesis")[0]
                index = classes[hypothesis_one.getElementsByTagName("context")[0].firstChild.data]
                result.append(f"{index} {bbox_string}")

        if group_one is not None:
            hypothesis_one = group_one.getElementsByTagName('hypothesislist')[0]
            hypothesis_context = hypothesis_one.getElementsByTagName('context')[0].firstChild.data
            group_box = group_one.getElementsByTagName('box')[0]
            yolo_group_bbox = []

            xc = safe_division(int(group_box.getAttribute('xc')), image_width)
            yc = safe_division(int(group_box.getAttribute('yc')), image_height)
            w = safe_division(int(group_box.getAttribute('w')), image_width)
            h = safe_division(int(group_box.getAttribute('h')), image_height)

            yolo_group_bbox.append(xc)
            yolo_group_bbox.append(yc)
            yolo_group_bbox.append(w)
            yolo_group_bbox.append(h)
            bbox_string = " ".join([str(x) for x in yolo_group_bbox])
            index = classes[hypothesis_context]
            result.append(f"{index} {bbox_string}")

        # Write YOLO TXT
        if result:
            # generate a YOLO format text file for each xml file
            with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
                f.write("\n".join(result))






