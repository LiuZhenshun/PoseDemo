import os
import json
import shutil

JsonPath = "/media/hkuit164/Backup/ThermalProject/2022_11_03_cloudy_dataset/thermal/annotations/val.json"
FolderPath = "/media/hkuit164/Backup/ThermalProject/2022_11_03_cloudy_dataset/thermal/images"
OuputPath = "/media/hkuit164/Backup/ThermalProject/2022_11_03_cloudy_dataset/thermal/images/val"
move = True

JsonObj = open(JsonPath, "r")
Data = json.load(JsonObj)

for imageObj in Data["images"]:
    source = os.path.join(FolderPath, imageObj["file_name"])
    destination = os.path.join(OuputPath, imageObj["file_name"])
    if move:
        shutil.move(source, destination)
    else:
        shutil.copyfile(source, destination)
