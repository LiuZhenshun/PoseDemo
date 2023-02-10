

detector_cfg = "/media/hkuit164/Backup/OneDrive_1_2-9-2023/yolov3-spp-1cls.cfg"
detector_weight = "/media/hkuit164/Backup/OneDrive_1_2-9-2023/backup90.pt"

RgbVideoCap = 'rtsp://admin:fyp202020@192.168.8.111:554/Streaming/Channels/101/?transportmode=unicast --input-rtsp-latency=0'
TherVideoCap = 'rtsp://admin:fyp202020@192.168.8.111:554/Streaming/Channels/201/?transportmode=unicast --input-rtsp-latency=0'

pose_weight = "/media/hkuit164/Backup/latest.pth"
pose_model_cfg = ""
pose_data_cfg = ""

#input_src = TherVideoCap
input_src = "/media/hkuit164/Backup/free_1_thermal (online-video-cutter.com).mp4"
output_src = "/media/hkuit164/Backup/free_1_thermal (online-video-cutter.com)_detectionresult.mp4"
out_size = (1080, 720)
show_size = (1080, 720)
show = True

write_json = False
json_path = ""
filter_criterion = {}

