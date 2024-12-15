import cv2
import config
from lib.utils import draw_obj_bboxes, draw_disease_bboxes
from ultralytics import YOLO

def inference_with_yolo(checkpoint, img, whichyolo):
    #checkpoint = config.path_obj_yolo
    model = YOLO(checkpoint)
    result = model(img)
    bboxes = result[0].boxes
    result_img = img.copy()
    if whichyolo == "obj":
        draw_obj_bboxes(result_img, bboxes)
    elif whichyolo == "disease":
        draw_disease_bboxes(result_img, bboxes)
    #return {"img":result_img.tolist()}
    return {"ai":result_img.tolist(),\
            "bboxes":bboxes.xyxy.detach().numpy().tolist(), 
            "classes":bboxes.cls.detach().numpy().tolist()}

