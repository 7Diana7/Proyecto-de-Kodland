from flask import Flask,request, send_file
from werkzeug.utils import secure_filename
import os
import Deteccion as detections
app = Flask(__name__)
Deteccion_objetos = detections
carpeta_destino = 'img'

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png','jpg','jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        scanned_path = Deteccion_objetos(file_path)
    return send_file(scanned_path, as_attachment = True)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
