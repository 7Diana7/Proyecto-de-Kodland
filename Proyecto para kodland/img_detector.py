from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from flask import Flask,request, send_file, render_template
from werkzeug.utils import secure_filename
import os
from Deteccion import Deteccion, result

app = Flask(__name__)
carpeta_destino = 'img'
Deteccion_objetos = Deteccion()
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}
resultado = result()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload')
def upload_file(image):
    file = request.files[image]
    if file and allowed_file(file.filename):
        fileNAME = secure_filename(file.filename)
        file_path = os.path.join(app.config[UPLOAD_FOLDER], fileNAME)
        file.save(file_path)
        scanned_path = Deteccion_objetos(file_path)
    return send_file(scanned_path, as_attachment = True)

@app.route('/answer')
def Analyse_obj(road_objects):
    if road_objects:
        return resultado
    else:
        print("No se detectaron objetos.")

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
