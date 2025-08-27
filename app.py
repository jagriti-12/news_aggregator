from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# Get API key from environment variable
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "your-api-key")

# Categories we will support
CATEGORIES = ["business", "technology", "sports", "health", "entertainment", "science"]

@app.route("/", methods=["GET", "POST"])
def home():
    category = request.form.get("category", "technology")  # default = tech
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    return render_template("index.html", articles=articles, categories=CATEGORIES, active=category)

if __name__ == "__main__":
    app.run(debug=True)
