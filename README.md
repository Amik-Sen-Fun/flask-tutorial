# Flask-tutorial
Trying to learn Flask :p

## Bit about Flask 
Flask is a micro web framework writen in Python. Micro web framework means it is a very light weight and things can be imported on the go.

Pinterest and LinkedIn are based on flask (wowww)

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

