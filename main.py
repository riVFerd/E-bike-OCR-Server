import cv2
import numpy as np
from flask import Flask, render_template, request, jsonify, json
from flask_ngrok import run_with_ngrok

import ocr_ktm
import ocr_ktp

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ping')
def test_server():
    return jsonify({'result': 'success', 'msg': 'This is a test server', 'status': 200})


@app.route('/test_api')
def test_api():
    return render_template('test_api.html')


@app.route('/ocr_ktm', methods=['POST'])
def upload_file_ktm():
    if 'image' not in request.files:

        json_content = {
            'message': "image is empty"
        }
    else:
        imagefile = request.files['image'].read()
        npimg = np.frombuffer(imagefile, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        cv2.imwrite('image.jpg', image)

        ktm_model = ocr_ktm.main()

        json_content = json.loads(ktm_model.toJson())

    # print(json_content)
    python2json = json.dumps(json_content)
    return app.response_class(python2json, content_type='application/json')


@app.route('/ocr_ktp', methods=['POST'])
def upload_file_ktp():
    if 'image' not in request.files:

        json_content = {
            'message': "image is empty"
        }
    else:
        imagefile = request.files['image'].read()
        npimg = np.frombuffer(imagefile, np.uint8)
        image = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

        cv2.imwrite('image.jpg', image)

        ktp_model = ocr_ktp.main()

        json_content = json.loads(ktp_model.toJson())

    # print(json_content)
    python2json = json.dumps(json_content)
    return app.response_class(python2json, content_type='application/json')


if __name__ == '__main__':
    # run_with_ngrok(app)
    app.run(host='0.0.0.0')
