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
- 
