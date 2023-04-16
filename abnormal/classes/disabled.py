import numpy as np


class DisabledHandler:
    def __init__(self):
        pass

    def process(self, ids, boxes, kps, kps_scores):
        return np.zeros(len(boxes))



