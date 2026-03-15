from flask import send_from_directory

from server.create_app import create_app
from server.get_photos import get_photos

app = create_app()


@app.route("/")
def index():
    photos = get_photos()
    return send_from_directory("../client/www", "index.html")
