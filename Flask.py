import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename, redirect
import csv

UPLOAD_FOLDER = 'F:/work/fyp/pycharm/static/UPLOAD_FOLDER'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# APP_STATIC = os.path.join(APP_ROOT, 'static')
# @ signifies a decorator - way of saying wrap a function and modifying its behavior
# route function takes the url in () and returns what is returned by function index
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file1 = request.files['file']
        filename = secure_filename(file1.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file=filename.split('.')
        print(UPLOAD_FOLDER+"/"+filename)
        handle=open(UPLOAD_FOLDER+"/"+filename)
        if file[1] == 'txt':
            content = handle.read()
            sentences = 0
            words = 0
            sentence=content.replace('\n', ' ').rstrip()
            lines=content.count('\n')

            for s in sentence.split('. ') or sentence.split('? '):  # spliting on the basis of . with a space for the confirmation of a new sentence
                sentences = sentences + 1  # counting number of sentences

            for word in sentence.split(' '):
                words=words+1

            #print (lines)
            #print (sentences)
            print(words)
            print("content is "+content)
        if file[1]=='csv':
            r = csv.reader(handle)
            content=""
            lines=0
            sentences = 0
            words=0
            for rows in r:
                lines += 1
                for cols in rows:
                    print(cols)
                    content=content+cols+" "
                    for s in cols.split('. ')or sentence.split('? '):  # spliting on the basis of . with a space for the confirmation of a new sentence
                        sentences += 1

                    for word in cols.split(' '):
                        words=words+1
                content=content+'\n'
                print(content)


        return render_template("index.html", content=content, lines=lines, sentences=sentences, words=words)

    return render_template("index.html")



if __name__ == "__main__":
    app.run()
