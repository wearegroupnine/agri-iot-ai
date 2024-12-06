import cv2
import config
from lib.utils import draw_bboxes
from ultralytics import YOLO

def inference_obj_yolo(img):
    checkpoint = config.path_obj_yolo
    model = YOLO(checkpoint)
    result = model(img)
    bboxes = result[0].boxes
    result_img = img.copy()
    draw_bboxes(result_img, bboxes)
    return {"img":result_img.tolist()}
    #return {"bboxes":bboxes.tolist(), "classes":classes.tolist()}

