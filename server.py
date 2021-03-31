from app import create_app
from flask import render_template
import json

app = create_app()

# open config file to get host and port

CONFIG_FILE = open("config.json", "r")

config = json.loads(CONFIG_FILE.read())

host = config.get("HOST", "127.0.0.1")
port = config.get("PORT", 5000)
debug = config.get("DEBUG", False)

# index route defined here

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host, port, debug=debug)