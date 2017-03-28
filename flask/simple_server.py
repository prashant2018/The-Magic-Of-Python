'''
For installation : 

#for python 2.7
sudo pip install Flask

#for python 3
sudo pip3 install Flask


We will make a simple server which will display some html files
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mozilla"

#variable rules. Passing values to url
@app.route('/disp/<name>')
def showName(name):
	return "Hi "+name


if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8000')