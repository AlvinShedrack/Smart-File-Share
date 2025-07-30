import os
import webbrowser
from threading import Timer
from flask import Flask, request, jsonify, send_from_directory

# Start Flask App
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    return jsonify({"filename": file.filename})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Automatically open the browser
def open_browser():
    webbrowser.open_new('http://192.168.100.140:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()  # open after 1 second
    app.run(host='0.0.0.0', port=5000)
