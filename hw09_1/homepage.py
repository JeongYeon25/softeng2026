from turtle import pd
import pandas as pd
from flask import Flask, render_template
from requests import post

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blog_list")
def page1():
    # posts = [
    #     {"title": "제목제목1", "content": "내용내용1"},
    #     {"title": "제목제목2", "content": "내용내용2"},
    #     {"title": "제목제목3", "content": "내용내용3"},
    # ]
    df = pd.read_csv("hw08/blog_data.csv",encoding="utf-8")
    posts=[]
    # for i, row in df.iterrows():
    #     posts.append(row)

    post = df.to_dict(orient="records")
    return render_template("blog_list_simple.html", posts=post)



@app.route("/about")
def page2():
    return render_template("about_me.html")


if __name__ == "__main__":
    app.run(debug=True)