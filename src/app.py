import sys
from flask import Flask
import structlog
from decouple import config

log = structlog.get_logger()
app = Flask(__name__)


def main():
    log.info("starting sample flask server")
    app.run(host="0.0.0.0", debug=True, port=80)


@app.route("/")
def hello():
    log.info("running hello route")
    app_name = config("KS_APP_NAME")
    version = config("VERSION")

    message = "Hello World from Flask in a Docker container app name {0} version {1}".format(app_name, version)
    return message


if __name__ == "__main__":
    main()
