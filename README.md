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
```html5
<!---previous formatting stuff --->
  {{% for post in posts %}}
	<h1>{{post.title}}</h2>
	<p>{{post.content}}</p>
  {{% endfor %}}

```
