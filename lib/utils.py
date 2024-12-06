import cv2
import numpy as np

color_dict = {0:(255, 255,255), 1:(0, 255, 0)}
class_dict = {0 : "ripe", 1 : "unripe"}

def draw_bboxes(img, bboxes):
    classes = bboxes.cls.detach().cpu().numpy()
    conf = bboxes.conf.detach().cpu().numpy()
    boxes = bboxes.xyxy.detach().cpu().numpy()
    for cls, conf, box in zip(classes, conf, boxes):
        x1, y1, x2, y2 = box.astype(np.uint32)
        p1, p2 = (x1, y1), (x2, y2)

        cls_name = class_dict[int(cls)]
        color = color_dict[int(cls)]
        cv2.rectangle(img, p1, p2, color, thickness=2)
        if int(cls) == 0:
            cv2.rectangle(img, (x1, y1-15),  (x1+70, y1), color=color, thickness=-1)
        else:
           cv2.rectangle(img, (x1, y1-15),  (x1+80, y1), color=color, thickness=-1)
        text = f"{cls_name} {conf:.2f}"
        cv2.putText(img, text, (x1+5, y1-5), cv2.FONT_HERSHEY_PLAIN, 0.8, color=(0, 0, 0))
