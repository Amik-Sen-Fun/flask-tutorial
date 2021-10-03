from flask import Flask, render_template 

all_posts = [{'title': 'Post 1', 'content': 'This is content for Post 1'},
        {'title':'Post 2', 'content':'This is the contet of post 2'}]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts = all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello_user(name, id):
    return "Hello "+name+", your id is "+str(id)

@app.route('/home')
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)


