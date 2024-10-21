import os
from flask import Flask, request, render_template, flash, redirect, url_for, send_from_directory
from markupsafe import escape
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'rar', 'zip', 'tar', 'gz', 'tgz', 'exe'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

@app.route("/")
def index():
    content = open('content','r').read()
    return render_template('index.html', content=content)

@app.post("/save")
def save():
    content = request.json.get('content')
    content = open('content','w').write(content)
    return 'saved'

@app.route('/upload',methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        file_list = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('files.html', files=file_list)
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(request.url)

@app.route('/files')
def list_files():
    # 获取目录下的文件列表
    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    # 渲染模板并传递文件列表作为参数
    return render_template('files.html', files=file_list)
        
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

