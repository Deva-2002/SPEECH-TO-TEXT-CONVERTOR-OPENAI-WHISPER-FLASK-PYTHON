from flask import Flask,request,redirect,url_for,jsonify
import openai
import os

app=Flask(__name__)

app.config["UPLOAD_FOLDER"]="static";

@app.route('/',methods=['GET','POST'])
def upload_file():
    if request.method=="POST":
        file=request.file['file']
        if file:
            filename=file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            model=whisper.load_model("base")
            result=model.translate("Recording.M4a")
            return jsonify(result)
            # return redirect(url_for('upload_file',filename=filename))
    return '''
    <!doctype html>
    <title>Upload an audio file</title>
    <h1>Upload an audio file</h1>
    <form method=post enctype=mutipart/form-data>
    <input type=file name=file>
    <input type=submit value=Upload>
    </form>
    '''
   

        

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
