from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/yo/<argu>")
def callme(argu):
	d = {'name':argu,'age':22}
	return render_template('index.html',argu=d)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='8000')