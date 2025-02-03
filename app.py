from flask import Flask,render_template, redirect, request
from dbhelper import *

uploadfolder = "static/img"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = uploadfolder
app.config['SECRET_KEY'] = "qwerty12345"

@app.route('/saveinformation', methods=['GET','POST'])
def saveinformation()-> None:
    idno:str = request.args.get('idno')
    lastname:str = request.args.get('lastname')
    firstname:str = request.args.get('firstname')
    course:str = request.args.get('course')
    level:str = request.args.get('level')
    
    
    file = request.files['webcam']
    imagename = uploadfolder+"/"+idno+".jpeg"
    file.save(uploadfolder+"/"+idno+".jpeg")
    ok:bool = add_record('students', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level, image=imagename)
    message = "Student Added" if ok else "Error Adding Student"

@app.route("/") 
def index()->None:
    return render_template("index.html",pagetitle="Student information")
    
if __name__=="__main__":
    app.run(debug=True)