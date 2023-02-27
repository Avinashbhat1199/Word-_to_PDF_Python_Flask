from flask import Flask ,render_template ,send_from_directory ,request
from werkzeug.utils import secure_filename

app=Flask(__name__)
@app.route('/')

def index():
    return render_template('index1.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(port=5003, debug = True)