from flask import render_template, jsonify, request
from app import app

source_url_prefix = "http://localhost:4000/api/mobile/file?fileDirectory="


@app.route("/video", methods=["GET"])
def video():
    source_dir = request.args.get("src")
    source_dir = \
        source_dir or \
        "uploads/qwer/5befd553dab03c4f3c5acbb3/soccer1.webm"
    return render_template("video.html", source_url="{}{}".format(source_url_prefix, source_dir))


@app.route("/box", methods=["GET"])
def box():
    return render_template("box.html")


@app.route("/image", methods=["GET"])
def image():
    source_url_prefix = "http://localhost:4000/api/mobile/file?fileDirectory="
    source_dir = request.args.get("src")
    source_dir = \
        source_dir or \
        "uploads/qwer/5befd553dab03c4f3c5acbb3/soccer1.webm"
    return render_template("image.html", source_url="{}{}".format(source_url_prefix, source_dir))


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "no": "such page",
        "page": "not found",
        "code": "404"
    })


@app.errorhandler(403)
def forbidden(error):
    return jsonify({
        "page": "forbidden",
        "code": "403"
    })
