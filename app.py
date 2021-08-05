from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    if request.headers.getlist("X-Forwarded-For"):
        #GIP=request.headers.getlist("X-Forwarded-For")[0].split('', 1)
        GIP=request.headers.getlist("X-Forwarded-For")[0].split(',')[0]
    else:
        GIP=request.environ['REMOTE_ADDR']

    renderpage = render_template("app.html", gip=GIP)
    return renderpage

