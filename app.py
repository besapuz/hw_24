from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

from utils import *

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json
    file_name = data["filename"]
    path_file = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(path_file):
        raise BadRequest

    return jsonify(reads_file(data))
