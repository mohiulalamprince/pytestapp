from flask import Flask, render_template
from flask import request, redirect, jsonify, url_for
from werkzeug.utils import secure_filename
from parser import get_file_content
from app import app
from os import listdir
from os.path import isfile, join
import time
import os

START_H1 = "<h1>" + "TOTAL Transactions : " 
END_H1 = "</h1>" 
START_H3 = "<h3>Transaction : "
END_H3 = "</h3>"

UPLOAD_FOLDER = "UPLOAD_FOLDER"

BAD_REQUEST_CODE = 400
MESSAGE = "message"

ERROR = "ERROR"
ERROR_MESSAGE_0001 = 'No file part in the request'
ERROR_MESSAGE_0002 = 'No file selected for uploading'
ERROR_MESSAGE_0003 = 'Allowed file types are csv, prn'


ALLOWED_EXTENSIONS = set(['csv', 'prn'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file-upload', methods=['POST', 'GET'])
def upload_file():
    """This is a file upload rest api for {csv, prn} file. If you upload a {prn, csv} file 
    it will parse the file and convert the file as a html. 


    Parameters
    ----------
    file : file, required
        file represent a csv or prn file        
    """

    # check if the post request has the file part
    if request.method == 'POST':
        if 'file' not in request.files:
                resp = jsonify({MESSAGE : ERROR_MESSAGE_0001})
                resp.status_code = BAD_REQUEST_CODE
                return resp
        file = request.files['file']
        if file.filename == '':
                resp = jsonify({MESSAGE : ERROR_MESSAGE_0002})
                resp.status_code = BAD_REQUEST_CODE
                return resp
        if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                unique_name = str(time.time())
                file.save(os.path.join(app.config[UPLOAD_FOLDER], unique_name + "-" + filename))

                data = get_file_content(os.path.join(app.config[UPLOAD_FOLDER], unique_name + "-" + filename), filename)

                if data.startswith(ERROR):
                    resp = jsonify({MESSAGE: data}) 
                    resp.status_code = BAD_REQUEST_CODE
                    return resp
                return render_template('index.html', data=data)
        else:
                resp = jsonify({MESSAGE : ERROR_MESSAGE_0003})
                resp.status_code = BAD_REQUEST_CODE
                return resp
    else: 
        return render_template("file-upload.html")

@app.route('/all-transactions', methods=['GET'])
def all_transactions():
    """This is a rest api for over all over view of your all
    uploaded file or tranactions. 

    """

    mypath = app.config[UPLOAD_FOLDER]
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    contents = START_H1 + str(len(onlyfiles)) + END_H1 
    for filename in onlyfiles:
        seconds = filename.rsplit('-', 1)[0]
        contents += START_H3 + str(time.ctime(float(seconds))) + END_H3
        contents += get_file_content(os.path.join(app.config[UPLOAD_FOLDER], filename), filename)
        
    return render_template('index.html', data=contents)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
