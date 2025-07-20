from flask import Flask, request, render_template, send_file
import os
from crypto_utils import encrypt_file, decrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return 'No selected file'

    filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    uploaded_file.save(filepath)

    # Encrypt file
    encrypted_path = encrypt_file(filepath)

    return f'File encrypted and saved as: {os.path.basename(encrypted_path)}'

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return 'File not found'

    # Decrypt
    decrypted_path = decrypt_file(filepath)
    return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
