from flask import Flask, render_template, request
import requests, os

app = Flask(__name__)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsapi.org/v2/top-headlines"

CATEGORIES = ["technology", "business", "sports", "health"]

@app.route("/", methods=["GET", "POST"])
def index():
    category = "technology"
    page = int(request.args.get("page", 1))  # default page 1

    if request.method == "POST":
        category = request.form.get("category", "technology")
        page = 1  # reset page when category changes

    params = {
        "apiKey": NEWS_API_KEY,
        "country": "us",
        "category": category,
        "pageSize": 6,   # 6 per page
        "page": page
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    articles = data.get("articles", [])

    return render_template(
        "index.html",
        categories=CATEGORIES,
        articles=articles,
        active=category,
        page=page
    )
