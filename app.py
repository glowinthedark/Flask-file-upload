#!/usr/bin/env python3
from pathlib import Path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods=['GET', 'POST'])
def save_file():
    content = "error"
    
    if request.method == 'POST':
        fileStorage = request.files['file']
        filename = secure_filename(fileStorage.filename)

        dest = Path(app.config['UPLOAD_FOLDER'])/filename
        dest.parent.mkdir(exist_ok=True, parents=True)
        
        with dest.open('wb') as fo:
            fileStorage.save(fo)

        content = dest.read_text(encoding='utf-8')

    return render_template('content.html', content=content)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
