# app.py
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    content = db.Column(db.Text)

db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    text = request.form['text']
    if len(text) > 10000:
        return "Text is too long, maximum 10,000 characters allowed."
    post_id = str(uuid.uuid4())
    new_post = Post(id=post_id, content=text)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for('show_post', post_id=post_id))

@app.route('/<post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    highlighted_text = highlight(post.content, guess_lexer(post.content), HtmlFormatter())
    return render_template('post.html', post=post, highlighted_text=highlighted_text)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    posts = Post.query.filter(Post.content.contains(query)).all()
    return render_template('search.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
