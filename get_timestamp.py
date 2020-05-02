from datetime import datetime, timezone
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return str(datetime.now().timestamp())