from flask import redirect
from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


def fetch_post_by_id(post_id):
    if 0 <= post_id < len(blog_posts):
        return blog_posts[post_id]
    return None


with open('fuckin_jsonfile.json', 'r') as file:
    blog_posts = json.load(file)


@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        content = request.form.get("content")

        new_post = {
            "title": title,
            "author": author,
            "content": content
        }

        blog_posts.append(new_post)

        with open('fuckin_jsonfile.json', 'w') as file:
            json.dump(blog_posts, file)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id):
    if 0 <= post_id < len(blog_posts):
        del blog_posts[post_id]
        with open('fuckin_jsonfile.json', 'w') as file:
            json.dump(blog_posts, file)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
