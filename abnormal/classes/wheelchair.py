import numpy as np


class WheelchairHandler:
    def __init__(self):
        self.hw_threshold = 0.7128

    def process(self, ids, boxes, kps, kps_scores):
        # If Bounding Box is vertical rectangle, ResultVec related position is Ture;
        # If horizontal, ResultVec related position is False;
        ResultVec = np.zeros(len(boxes))
        for index, bbox in enumerate(boxes):
            print("ratio:", (bbox[2] - bbox[0]) / (bbox[3] - bbox[1]))
            print("bbox:", bbox)
            if (bbox[2] - bbox[0]) / (bbox[3] - bbox[1]) > self.hw_threshold:
                ResultVec[index] = 1
            else:
                ResultVec[index] = 0
        return ResultVec




