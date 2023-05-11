import xml.etree.ElementTree as ET
import glob
import os

input_base_dir = "caviar_annotations/"
input_caviar_fighting_chase_jpg_dir = "Fighting/Fight_Chase/JPEGS/"
input_caviar_fighting_one_man_down_jpg_dir = "Fighting/Fight_OneManDown/JPEGS/"
input_caviar_fighting_fight_run_away1_jpg_dir = "Fighting/Fight_RunAway1/JPEGS/"
input_caviar_fighting_fight_run_away2_jpg_dir = "Fighting/Fight_RunAway2/JPEGS/"
input_caviar_fighting_chase_annotation_file_path = "Fighting/Fight_Chase/fcgt.xml"
input_caviar_fighting_one_man_down_annotation_file_path1 = "Fighting/Fight_OneManDown/fomdgt1.xml"
input_caviar_fighting_one_man_down_annotation_file_path2 = "Fighting/Fight_OneManDown/fomdgt2.xml"
input_caviar_fighting_one_man_down_annotation_file_path3 = "Fighting/Fight_OneManDown/fomdgt3.xml"
input_caviar_fighting_fight_run_away1_annotation_file_path = "Fighting/Fight_RunAway1/fra1gt.xml"
input_caviar_fighting_fight_run_away2_annotation_file_path = "Fighting/Fight_RunAway2/fra2gt.xml"

# identify all the xml files in the annotations folder (input directory)
tree = ET.parse(input_base_dir + input_caviar_fighting_chase_annotation_file_path)
root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

print(root[0][0].id)

height = root.find('Fight_Chase')

for obj in root.findall('object'):
    label = obj.find("name").text
    # check for new classes and append to list
    # if label not in classes:
    #     classes.append(label)
    # index = classes.index(label)
    # pil_bbox = [int(x.text) for x in obj.find("bndbox")]
    # yolo_bbox = xml_to_yolo_bbox(pil_bbox, width, height)
    # # convert data to string
    # bbox_string = " ".join([str(x) for x in yolo_bbox])
    # result.append(f"{index} {bbox_string}")

# if result:
#     # generate a YOLO format text file for each xml file
#     with open(os.path.join(output_dir, f"{filename}.txt"), "w", encoding="utf-8") as f:
#         f.write("\n".join(result))

