import wget
from botocore.exceptions import ClientError
from flask import Flask, request, render_template,Response,send_file
from botos3.aws import AwsFunctions



external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    try:
        file = request.files["file"]
        size = len(file.read())
        delete_time = request.form["time"]
        IP = request.remote_addr
        filename = file.filename
        extension = filename.split(".")[1]
        file.save(filename)

        sec_key =  AwsFunctions.upload(filename, extension, delete_time, size, IP)
        return render_template("upload.html",secret_key=sec_key)
    except ClientError as error:
        return error


@app.route("/download", methods=["POST"])
def dowload():
    key = request.form["key"]
    IP = request.remote_addr

    file = AwsFunctions.download(key, IP)

    return render_template("download.html",secret_key=file)

if __name__ == '__main__':
    app.run(port=5000)
