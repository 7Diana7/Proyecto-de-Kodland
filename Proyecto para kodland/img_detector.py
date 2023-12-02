from flask import Flask,request, send_file
from imageai.Detection import ObjectDetection
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from PIL import Image, ImageOps
import numpy as np
import os
import Deteccion as detections
app = Flask(__name__)
Deteccion_objetos = detections

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

file = request.files['file']
filename = secure_filename(file.filename)

@app.run('upload', methods=['POST'])
def upload_file():
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        scanned_path = Deteccion_objetos(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return send_file(scanned_path, as_attachment = True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)