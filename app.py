from flask import Flask, render_template, request, redirect 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

all_posts = [{'title': 'Post 1', 'content': 'This is content for Post 1'},
        {'title':'Post 2', 'content':'This is the contet of post 2'}]

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    author = db.Column(db.String(20), nullable = False, default = 'N/A')
    post_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

  # Now instead of giving each data point some random name we can give proper name as
    def __repr__(self):
        return 'Blog Post ' + str(self.id)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods = ['GET', 'POST'])
def posts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title = post_title, content = post_content, author = post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.post_date.desc()).all()
        return render_template('posts.html', posts = all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post_delete = BlogPost.query.get_or_404(id)
    db.session.delete(post_delete)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    post_edit = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post_edit.title = request.form['title']
        post_edit.content = request.form['content']
        post_edit.author = request.form['author']
        db.session.commit()
        return redirect('/posts')
    else: 
        return render_template('edit.html', post = post_edit)

@app.route('/posts/new', methods = ['GET', 'POST'])
def newposts():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title = post_title, content = post_content, author = post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else :
        return render_template('new.html')


@app.route('/home/users/<string:name>/posts/<int:id>')
def hello_user(name, id):
    return "Hello "+name+", your id is "+str(id)

@app.route('/home')
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)


