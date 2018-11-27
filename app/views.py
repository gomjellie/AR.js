from flask import render_template, jsonify, request
from app import app
from random import randint

source_url_prefix = "https://colaboapp.cc/api/mobile/static?fileDirectory="


@app.route("/video", methods=["GET"])
def video():
    source_dir = request.args.get("src")
    source_dir = \
        source_dir or \
        "uploads/qwer/5befd553dab03c4f3c5acbb3/soccer1.webm"
    rand_val = randint(0, 255555555)
    return render_template("video.html", source_url="{}{}".format(source_url_prefix, source_dir), rand=rand_val)


@app.route("/box", methods=["GET"])
def box():
    return render_template("box.html")


@app.route("/3dmodel", methods=["GET"])
def three_dimension_model():
    source_dir = request.args.get("src")
    object_url = "{}{}".format(source_url_prefix, source_dir)
    mtl_url = object_url.replace("obj", "mtl")
    return render_template("3dmodel.html", object_url=object_url, mtl_url=mtl_url)

@app.route("/video_chroma_key", methods=["GET"])
def video_chroma_key():
    source_dir = request.args.get("src")
    return render_template("video_chroma_key.html", source_url="{}{}".format(source_url_prefix, source_dir))


@app.route("/image", methods=["GET"])
def image():
    source_dir = request.args.get("src")
    source_dir = \
        source_dir or \
        "uploads/qwer/5befd553dab03c4f3c5acbb3/soccer1.webm"
    return render_template("image.html", source_url="{}{}".format(source_url_prefix, source_dir))

@app.route("/joowon", methods=["GET"])
def joowon():
    return render_template("joowon.html")

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
