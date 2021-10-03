# Flask-tutorial
Trying to learn Flask :p

## Bit about Flask 
Flask is a micro web framework writen in Python. Micro web framework means it is a very light weight and things can be imported on the go.

Pinterest and LinkedIn are based on flask (wowww)

## Virtual Environement Setup 

Since we might be installing some packages and stuff it is better to maintain those files in a virtual environment and work with them.

To install the python3 virtual environment type the following code in terminal

```
python3 -m pip install --user --upgrade pip
python3 -m pip --version # to check the pip version
python3 -m pip install --user virtualenv
```

To create a virtual environment for a project:
```
python3 -m venv env_name 
// Try to keep this in .gitignore file
```

To activate the virtial env type:
```
source env_name/bin/activate
```
To deactivate the virtual env type:
```
deactivate
```


## Getting Started
To install flask simply do 

```python
pip install flask
flask --version # to check the version 
```
Now create a file names app.py and write 

```python
from flask import Flask

#intialisation of the app
app = Flask(__name__)
@app.route('/') # Here you write your website domain also
def hello():
  return "Hello World"

if __name__ == "__main__":
  app.run(debug = True) # to enable the debug mode
```
## Advanced URL Routing
- We can also add multiple routes to one function as shown below

```python
@app.route('/')
@app.route('/home')
def hello():
  return "Hello World"

# Now '/' and '/home' would acces the hello function
```
- In Debug mode server is automatically reloaded
- To get information from the url to the python function we access it like

```python
@app.rooute('/home/<string:name>')
def hello(name):
  return "Hello, " + name
```
Once we have defined a basic structure to run the application we just type the following in the terminal
```
python app.py
```
 
> The type of the URl data type can be <int>, <float> etc. Also we can have multiple such variables

- We can make functions specifically for a partiular requests like post, get, out or delete

```python
@app.route('/', methods = ['GET'])
def get_only():
	return "Only Showing Get Requests"

# We can also have multiple such request for a single function as

@app.route('/', methods = ['GET','POST'])
def get_only():
        return "Only Showing Get and Post Requests"

``` 
## Adding Basic Front End templates

- Here we will add HTML and CSS files for our website. The string that we were sending instead of that if we send HTML syntax then also the app woulld work, but it is not really good way so we need to link it to HTML files and CSS stuff.
- For this we will use Templates. For that make a folder named **templates** and make html files there. To render this file we write the syntax as :

```python
from flask import Flask, render_template  # import the renderer

@app.route('/')
def index():
  return render_template('index.html') # Renders the 'index.html' file in templates
``` 

- Similar to django we can create template inheritance and similar looping and variable stuff can be done in FLask also as both work on jinja. For understanding see the _base.html_ and then _index.html_ and observe the basic concept
  
- To send data to the front end, we simply send the data from the app.py part to the template as shown below:

```python
all_posts = [{'title': 'Post1', 'content': 'This is content of post 1'}]
@app.route('/posts')
def showPosts():
  return render_template('posts.html', posts = all_posts)
```
Now to access all the posts we make the following modifications in the post.html file which is done in jinja and are similar to django
```html
<!---previous formatting stuff --->
  {% for post in posts %}
	<h1>{{post.title}}</h2>
	<p>{{post.content}}</p>
  {% endfor %}
```
- Similarly we can use if statememt also
```python
all_posts = [{'title': 'Post1', 'content': 'This is content of post 1','author': 'Amik'},
{'title': 'Post1', 'content': 'This is content of post 1'}]
@app.route('/posts')
def showPosts():
  return render_template('posts.html', posts = all_posts)
```
Now if we wanna print the author's name only if it is present then we write
```html
<!---previous formatting stuff --->
  {% for post in posts %}
        <h1>{{post.title}}</h2>
	{% if post.author %}
		<h3>By : {{post.author}}</h3>
	{% else %}
		<h3>By : N/A</h3>
	{% endif %}
        <p>{{post.content}}</p>
  {% endfor %}
```
## Adding Static Files to our website
- The static files include css, javasript files, and images. So, we create a **static** folder and then, work accordingly as shown in the code
- To include the static files, do href similar to normal HTML, but we can also use a jinja varient to write the same URL and the command is as follows:

```html
<link rel = "stylesheet" href = "static/css/main.css">
        <!--Below is the jinja syntax to get the url for the file -->
<link rel = "stylesheet" href = "{{url_for('static', filename = 'css/main.css')}}">
```

## Adding a Database to our Webpage
Flask doesn't comes with a database integration method like django, so we need to download a third party library known as _sqlalchemy_ to get the database facilities. To download sqlalchemy use the following command

```
pip install flask-sqlalchemy
```
- Now in the **app.py** file import the library as:

```python 
from flask_sqlalchemy import SQLAlchemy

# now add a config file to locate the database which is defined as:

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db' # post is DB name

# In the app if you are using any other DB replace 'sqlite' with that
# Also the the three '/' means relative position of the database
# For the absolute path of the DB use four '/'

db = SQLAlchemy(app)
```
- Now, flask follows a MVC (Model View Controller) architecture, so we need to define classes that will be used for the database.

```python
from datetime import datetime
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    author = db.Column(db.String(20), nullable = False, default = 'N/A')
    post_date = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

  # Now instead of giving each data point some random name we can give proper name as
    def __repr__(self):
        return 'Blog Post' + str(id)
```
- Now, this just the design of the Database and the data type of data but this database needs to be created. To do that do the following steps. 

```python
# Go to the app folder and open terminal and open python 

# To make the app db
>>> from app import db
# because in app we declared database as db
>>> db.create_all()

# Now to do operations we import the required Model:
>>> from app import BlogPost

# Now to get all the members of a model:
>>> BlogPost.query.all()

# To add data to the database:
>>> db.session.add(BlogPost(title = 'Blog Post 1', content = 'Content of Blog Post 1', author = 'Amik'))

# To access specific data we write:
>>> BlogPost.query.all()[0]
>>> BlogPost.query.all()[0].title # To get the title of query 0

# To save changes of the session in the DB for future use do:
>>> db.session.commit()
```

## Different HTTP Methods on the Database

- To take input from the frontend, create a form like :
```html
<h2>Create New Blog Post</h2>
<form action = '/posts' method = 'POST'>
        Title : <input type = 'text' name = title id = 'title'>
        <br>
        Post : <input type = 'text' name = 'content' id = 'content'>
        <br>
        Author : <input type = 'text' name = 'author' id = 'author'>
        <br>
        <input type = 'submit' value = 'Post'>
</form>
<hr>
``` 
- In the backend, change the method in the corresponding function to post and save the changes in the database as :
```python
from flask import Flask, render_template, redirect, request 
# ... the other stuff

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
```
- In the database, we can query objects based on certain requirements so let's look at some such commmands
```python
# To filter objects based on some condition
>>> BlogPost.query.filter_by(title = 'First Blog Post').all 

# To get an object with certain id
>>> BlogPost.query.get(1) # for object with id 1
>>> BlogPost.query.get_or_404(1) # to break the process if id is absent

# To delete an exiting entry from the database
>>> db.session.delete(BlogPost.query.get(1)) # To delete object with id 1
>>> db.session.commit() # To make the changes permanent

# To update an existing entry from database
>>> BlogPost.query.get(1).author = 'N/A' # changes author to 'N/A'
>>> db.session.commit() # to make the changes permanent

# To obtain data and order by in ascending and descending order
>>> BlogPost.query.order_by(BlogPost.post_date.desc()).all() # Descending order
>>> BlogPost.query.order_by(BlogPost.post_date).all() # Ascending order
```
- Now, to automate this process from the frontend, we define a function and a new route to carry out delete operations, so in **app.py** file define a new route as:

```python
@app.route('/posts/delete/<int:id>')
    post_delete = BlogPost.query.get_or_404(id)
    db.session.delete(post_delete)
    db.session.commit()
    return redirect('/posts')
@app.route('/posts/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    post_edit = BlogPost.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post = post_edit)
```
In the frontend file now add a button and link them to the new routes and create a new edit page
```html
<!--Other stuff above -->
 {% for post in posts %}
                <h2>{{ post.title }}</h2>
                <h4>By: {{post.author}} </h4>
                <p>{{post.content}}<p>
                <a href = '/posts/delete/{{post.id}}'>Delete</a>
                <a href = '/posts/edit/{{post.id}}'>Edit</a>
                <hr>
 {% endfor %}
```
The edit html is writen as:
```html
{% extends 'base.html' %}
{% block head %}
<title> Edit Post </title>
{% endblock %}

{% block body %}
<h1> Edit  Post </h1>

<hr>
<h2>Edit Blog Post</h2>
<form action = '/posts/edit/{{post.id}}' method = 'POST'>
        Title : <input type = 'text' name = title id = 'title' value = '{{post.title}}'>
        <br>
        Post : <input type = 'text' name = 'content' id = 'content' value = '{{post.content}}'>
        <br>
        Author : <input type = 'text' name = 'author' id = 'author' value = '{{post.author}}'>
        <br>
        <input type = 'submit' value = 'Post'>
</form>
<hr>
```
- These are the basic crud functions for a database in flask

