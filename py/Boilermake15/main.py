import os
from time import clock
from flask import Flask, url_for, render_template, send_file, redirect, request, Blueprint
from werkzeug import secure_filename
from scripter import Scripter

UPLOAD_FOLDER = '/res/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#admin = Blueprint('admin', __name__, static_folder='res')
scripter = Scripter()


def getSDtimediff():
    secs = int((clock() - scripter.SDtimestamp) % 60)
    mins = int((clock() - scripter.SDtimestamp) / 60)
    return `mins` + " mins, " + `secs` + " secs"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def redirect_front_page():
    return redirect("/front", code=302)

@app.route('/front')
def front_page():
    print(scripter.SDtimestamp)
    return render_template('/front.html', titles=scripter.SDtitles, links=scripter.SDlinks, githubHTML=scripter.GithubHTML, githubCSS=scripter.GithubCSS, timediff=getSDtimediff())

@app.route('/front/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        thisFile = request.files['file']
        if thisFile and allowed_file(thisFile.filename):
            filename = secure_filename(thisFile.filename)
            thisFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename = filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
        

@app.route('/Resume.html')
def resume_page():
    print(os.getcwd())
    #print(lookup_url('res', filename='Resume.pdf'))
    return render_template('Resume.html')
    #return send_file('Resume.10.27.15.pdf', mimetype='application/pdf', filename='res/Resume.10.27.15.pdf')

if __name__ == '__main__':
    app.run()