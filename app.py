from flask import Flask

import sensor_service


app = Flask(__name__)


@app.route("/")
def index():
    data = sensor_service.get_data()
    print data
