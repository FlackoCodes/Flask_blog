# from flask import Flask, render_template
# import requests
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def home():
#     response = requests.get("https://api.npoint.io/12cf49c647dc25d43d41").json()
#     titles = [d["title"] for d in response]
#     subtitles = [d["subtitle"] for d in response]
#     ids = [d["id"] for d in response]
#     # body = response["body"]
#     return render_template("index.html", titles=titles, subtitles=subtitles,ids =ids, zip=zip)

from flask import Flask, render_template,abort
import datetime as dt
import requests

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/12cf49c647dc25d43d41").json()
    titles = [d["title"] for d in response]
    subtitles = [d["subtitle"] for d in response]
    ids = [d["id"] for d in response]
    now = dt.datetime.now()
    year = now.year
    return render_template("home.html", year=year, titles=titles, subtitles=subtitles, ids=ids, zip=zip)


@app.route('/blog/<int:id>')
def blog(id):
    response = requests.get("https://api.npoint.io/12cf49c647dc25d43d41").json()
    if not response:
        abort(404)
    post = next((p for p in response if p["id"] == id), None)
    if post is None:
        abort(404)
    now = dt.datetime.now()
    year = now.year
    return render_template("posts.html", post=post, year=year)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

