import os
import cv2 as cv
from flask import Flask, render_template, request, send_from_directory, Response
from werkzeug.utils import secure_filename
from .img_processing import embossing, cartoon, pencilGray, pencilColor, oilPainting, enhance
import numpy as np
import sys

def create_app():
    app = Flask(__name__, static_url_path='')

    app.secret_key = os.urandom(24)
    app.config['RESULT_FOLDER'] = 'result_images'  # 반드시 폴더 미리 생성
    app.config['UPLOAD_FOLDER'] = 'uploads'  # 반드시 폴더 미리 생성

    @app.route('/upload_img/<filename>')
    def upload_img(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    @app.route('/result_img/<filename>')
    def result_img(filename):
        return send_from_directory(app.config['RESULT_FOLDER'], filename)

    @app.route('/img_result', methods=['GET', 'POST'])
    def img_result():
        if request.method == 'POST':
            f = request.files['file']

            # Save the file to ./uploads
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)
            file_name = os.path.basename(file_path)
            img = cv.imread(file_path)

            # processing
            style = request.form.get('style')
            if style == "Embossing" :
                output = embossing(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_emboss.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "Cartoon" :
                output = cartoon(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_cartoon.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "PencilGray" :
                output = pencilGray(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_pencilgray.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "PencilColor" :
                output = pencilColor(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_pencilcolor.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "OilPainting" :
                output = oilPainting(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_oil.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
            elif style == "Detail" :
                output = enhance(img)

                # Write the result to ./result_images
                result_fname = os.path.splitext(file_name)[0] + "_detail.jpg"
                result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
                fname = os.path.basename(result_path)
                cv.imwrite(result_path, output)
                return render_template('img_result.html', file_name=file_name, result_file=fname)
        return ''

    @app.route('/img_processing/', methods=['GET'])
    def img_processing():
        return render_template('img_processing.html')

    def construct_yolo_v3():
        f = open('coco_names.txt', 'r')
        class_names = [line.strip() for line in f.readlines()]

        model = cv.dnn.readNet('yolov3.weights', 'yolov3.cfg')
        layer_names = model.getLayerNames()
        out_layers = [layer_names[i - 1] for i in model.getUnconnectedOutLayers()]

        return model, out_layers, class_names

    def yolo_detect(img, yolo_model, out_layers):
        height, width = img.shape[0], img.shape[1]
        test_img = cv.dnn.blobFromImage(img, 1.0 / 256, (448, 448), (0, 0, 0), swapRB=True)

        yolo_model.setInput(test_img)
        output3 = yolo_model.forward(out_layers)

        box, conf, id = [], [], []  # 박스, 신뢰도, 부류 번호
        for output in output3:
            for vec85 in output:
                scores = vec85[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:  # 신뢰도가 50% 이상인 경우만 취함
                    centerx, centery = int(vec85[0] * width), int(vec85[1] * height)
                    w, h = int(vec85[2] * width), int(vec85[3] * height)
                    x, y = int(centerx - w / 2), int(centery - h / 2)
                    box.append([x, y, x + w, y + h])
                    conf.append(float(confidence))
                    id.append(class_id)

        ind = cv.dnn.NMSBoxes(box, conf, 0.5, 0.4)
        objects = [box[i] + [conf[i]] + [id[i]] for i in range(len(box)) if i in ind]
        return objects

    def capture_yolo():
        model, out_layers, class_names = construct_yolo_v3()  # YOLO 모델 생성
        colors = np.random.uniform(0, 255, size=(len(class_names), 3))  # 부류마다 색깔

        cap = cv.VideoCapture(0, cv.CAP_DSHOW)
        if not cap.isOpened(): sys.exit('카메라 연결 실패')

        while True:
            ret, frame = cap.read()
            if not ret: sys.exit('프레임 획득에 실패하여 루프를 나갑니다.')

            res = yolo_detect(frame, model, out_layers)

            for i in range(len(res)):
                x1, y1, x2, y2, confidence, id = res[i]
                text = str(class_names[id]) + '%.3f' % confidence
                cv.rectangle(frame, (x1, y1), (x2, y2), colors[id], 2)
                cv.putText(frame, text, (x1, y1 + 30), cv.FONT_HERSHEY_PLAIN, 1.5, colors[id], 2)

            cv.imshow("Object detection from video by YOLO v.3", frame)

            key = cv.waitKey(1)
            if key == ord('q'): break

    @app.route('/video_yolo')
    def video_yolo():
        return Response(capture_yolo(), mimetypes='multipart/x-mixed-replace; boundary=frame')

    @app.route('/webcam_yolo/')
    def webcam_yolo():
        return render_template('webcam_yolo.html')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app