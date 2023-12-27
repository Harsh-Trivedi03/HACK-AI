from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
import PyPDF2

app = Flask(__name__)
UPLOAD_FOLDER = r'C:\Users\Harsh\Desktop\hack-ai'  # Set your upload folder path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_resumes', methods=['POST'])
def upload_resumes():
    if 'resumes' not in request.files:
        return jsonify({"error": "No file part"}), 400
    files = request.files.getlist("resumes")
    resume_texts = {}
    for file in files:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        resume_texts[filename] = extract_text(file_path)
    # Send resume_texts to prompt_agent
    return jsonify({"message": "Resumes uploaded successfully", "data": resume_texts})

def extract_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''.join([reader.getPage(page).extractText() for page in range(reader.numPages)])
    return text

if __name__ == '__main__':
    app.run(debug=True)
