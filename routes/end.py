from flask import Blueprint, render_template, redirect, abort, request
import requests, json

URL = "http://localhost:3000"

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

endr = Blueprint('endr', __name__)

@endr.route('/encodeDecode', methods=["GET"])
def home():
    return render_template("end/index.html")

@endr.route('/encodeStr', methods=["GET", "POST"])
def encodeStr():
    if request.method == "POST":
        data = request.form
        pData = {
            'original': data['original'],
            'enc': data['algo']
        }

        try:
            uri = URL + "/encoder"
            r = requests.post(uri, data=json.dumps(pData), headers=newHeaders)
            if r.status_code == 200:
                data = json.loads(r.text)
                if data.get("error", False):
                    return render_template("end/decode.html", error=data['error'])
                return render_template("end/encode.html", result=data['encoded'])
        except Exception as e:
            print(e)
            return redirect('/encodeStr')
    return render_template("end/encode.html")


@endr.route('/decodeStr', methods=["GET", "POST"])
def decodeStr():
    if request.method == "POST":
        data = request.form
        pData = {
            'encoded': data['encoded'],
            'enc': data['algo']     
        }

        try:
            uri = URL + "/decoder"
            r = requests.post(uri, data=json.dumps(pData), headers=newHeaders)
            if r.status_code == 200:
                data = json.loads(r.text)
                if data.get("error", False):
                    return render_template("end/decode.html", error=data['error'])
                return render_template("end/decode.html", result=data['decoded'])
        except Exception as e:
            print(e)
            return redirect('/decodeStr')
    return render_template("end/decode.html")