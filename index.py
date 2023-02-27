import os
from flask import Flask, render_template, request,send_from_directory 
from werkzeug.utils import secure_filename




app = Flask(__name__)

UPLOAD_FOLDER = 'file/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
filename=''
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if 'image' not in request.files :
        return render_template('index.html')
    file = request.files['image']
    if file.filename == '':
           
            return render_template('index.html')
    else:
        
    
            filename =secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return render_template('download.html',filename=filename)
   
   
   
@app.route('/download/<filename>',methods=['GET','POST'])  
def download(filename):
 
    
    from docx2pdf import convert
    path=os.path.join(app.config['UPLOAD_FOLDER'],filename)

    convert(path)
    filename1=filename.replace(".docx",".pdf").replace(".dox",".pdf")


    return send_from_directory(directory=app.config['UPLOAD_FOLDER'],path=filename1,as_attachment=True)



if __name__ == '__main__':
    app.run(port=5002, debug = True)


    
  
