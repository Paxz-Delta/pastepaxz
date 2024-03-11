# app.py
from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)

posts = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    text = request.form['text']
    post_id = str(uuid.uuid4())
    posts[post_id] = text
    return redirect(url_for('show_post', post_id=post_id))

@app.route('/<post_id>')
def show_post(post_id):
    text = posts.get(post_id, 'Post not found')
    return render_template('post.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
