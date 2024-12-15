import config
from flask import Flask, request, jsonify
import numpy as np
from lib.yolo_inferences import inference_with_yolo
app = Flask(__name__)

@app.route('/obj_prediction', methods=['POST'])
def obj_prediction():
    data = request.json
    raw_image = np.array(data["img"]).astype(np.uint8)
    response = inference_with_yolo(config.path_obj_yolo, raw_image, whichyolo="obj")
    disease_res = inference_with_yolo(config.path_disease_yolo, raw_image, whichyolo="disease")
    response["disease"] = disease_res["ai"]
    return jsonify(response), 200

if __name__ == "__main__":
    config.reload_config()
    app.run(debug=True, port=6600)
