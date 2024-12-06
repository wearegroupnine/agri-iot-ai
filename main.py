import config
from flask import Flask, request, jsonify
import numpy as np
from lib.yolo_inferences import inference_obj_yolo
app = Flask(__name__)

@app.route('/obj_prediction', methods=['POST'])
def obj_prediction():
    data = request.json
    raw_image = np.array(data["img"]).astype(np.uint8)
    response = inference_obj_yolo(raw_image)
    return jsonify(response), 200


if __name__ == "__main__":
    config.reload_config()
    app.run(debug=True, port=6600)
