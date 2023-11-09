from flask import Flask, render_template, request, send_from_directory
import os
import cv2 as cv
from werkzeug.utils import secure_filename


def create_app():
    app = Flask(__name__, static_url_path='')

    app.secret_key = os.urandom(24)
    app.config['RESULT_FOLDER'] = 'result_images'   # 반드시 폴더 미리 생성
    app.config['UPLOAD_FOLDER'] = 'uploads'         # 반드시 폴더 미리 생성

    @app.route('/img_processing/', methods=['GET'])
    def img_processing():
        return render_template('img_processing.html')

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

            # reading the uploaded image
            img = cv.imread(file_path)

	# processing

	# Write the result to ./result_images
            result_fname = os.path.splitext(file_name)[0] + "_test.jpg"
            result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
            fname = os.path.basename(result_path)
            cv.imwrite(result_path, img)

            return render_template('img_result.html', file_name=file_name, result_file=fname)
        return ""

    @app.route('/')
    def index(): 
        return render_template('index.html')

    return app