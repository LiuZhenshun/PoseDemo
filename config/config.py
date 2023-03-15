

detector_cfg = "/home/sean/Desktop/1025+1103+1121/cfg/yolov3-spp-1cls.cfg"
detector_weight = "/home/sean/Desktop/1025+1103+1121/bs4/yolo_last.pt"

RgbVideoCap = 'rtsp://admin:fyp202020@192.168.8.111:554/Streaming/Channels/101/?transportmode=unicast --input-rtsp-latency=0'
TherVideoCap = 'rtsp://admin:fyp202020@192.168.8.111:554/Streaming/Channels/201/?transportmode=unicast --input-rtsp-latency=0'

pose_weight = "/home/sean/Desktop/1025+1103+1121/alphapose/latest.pth"
pose_model_cfg = "/home/sean/Desktop/1025+1103+1121/alphapose/model_cfg.json"
pose_data_cfg = "/home/sean/Desktop/1025+1103+1121/alphapose/data_cfg.json"

#input_src = TherVideoCap
output_src = ""
input_src = "/home/sean/Desktop/1025+1103+1121/xjl_wheelchair_thermal.mp4"
#output_src = "/media/hkuit164/Backup/free_1_thermal (online-video-cutter.com)_detectionresult.mp4"
out_size = (1280, 960)
show_size = (1280, 960)
show = True

write_json = True
json_path = "result.json"
filter_criterion = {}

