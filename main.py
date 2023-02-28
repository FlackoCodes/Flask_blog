from flask import Flask, render_template, abort
import datetime as dt
import requests

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    # Request data from external API
    response = requests.get("https://api.npoint.io/12cf49c647dc25d43d41").json()
    # Extract relevant data
    titles = [d["title"] for d in response]
    subtitles = [d["subtitle"] for d in response]
    ids = [d["id"] for d in response]
    # Get current year for use in template
    now = dt.datetime.now()
    year = now.year
    # Render template and pass in extracted data and current year
    return render_template("home.html", year=year, titles=titles, subtitles=subtitles, ids=ids, zip=zip)

# Blog post route with post ID parameter
@app.route('/blog/<int:id>')
def blog(id):
    # Request data from external API
    response = requests.get("https://api.npoint.io/12cf49c647dc25d43d41").json()
    # If no data was returned, raise 404 error
    if not response:
        abort(404)
    # Find the post with the specified ID
    post = next((p for p in response if p["id"] == id), None)
    # If post not found, raise 404 error
    if post is None:
        abort(404)
    # Get current year for use in template
    now = dt.datetime.now()
    year = now.year
    # Render template and pass in post data and current year
    return render_template("posts.html", post=post, year=year)

# Run app in debug mode on port 8000
if __name__ == "__main__":
    app.run(debug=True, port=8000)
