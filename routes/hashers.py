from flask import Blueprint, render_template, redirect, abort, request
import requests, json

URL = "http://localhost:3000"

newHeaders = {'Content-type': 'application/json', 'Accept': 'text/plain'}

hashers = Blueprint('hashers', __name__)

@hashers.route('/hasher', methods=["GET"])
def home():
    return render_template("hashers/index.html")

@hashers.route('/genHash', methods=["GET", "POST"])
def genHash():
    if request.method == "POST":
        data = request.form
        pData = {
            'original': data['original'],
            'method': data['algo']     
        }

        try:
            uri = URL + "/hasher"
            r = requests.post(uri, data=json.dumps(pData), headers=newHeaders)
            if r.status_code == 200:
                data = json.loads(r.text)
                if data.get("error", False):
                    return render_template("hashers/genHash.html", error=data['error'])
                return render_template("hashers/genHash.html", result=data['hash'])
        except Exception as e:
            return redirect('/genHash')
    return render_template("hashers/genHash.html")

