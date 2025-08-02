from flask import Flask, render_template, request, send_file
import os
from pisah_pdf import split_pdf_by_color

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['pdf_file']
        if file.filename.endswith('.pdf'):
            pdf_path = os.path.join(UPLOAD_FOLDER, 'uploaded.pdf')
            file.save(pdf_path)

            split_pdf_by_color(pdf_path)  # proses PDF

            return render_template('index.html', hasil=True)
    return render_template('index.html', hasil=False)

@app.route('/download/<filename>')
def download(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
