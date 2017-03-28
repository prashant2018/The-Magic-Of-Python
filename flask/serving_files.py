from flask import Flask,render_template,request
import subprocess as sp
import os

app = Flask(__name__)

@app.route("/")
def home():
	return "This is just the starting"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/yo/<argu>")
def callme(argu):
	d = {'name':argu,'age':22}
	return render_template('index.html',argu=d)
'''
@app.route("/song/<id>")
def playSong(id):
	if int(id) > 2 :
		return "Sorry unable to play"+id
	else:
		path = 'media/'+id+'.mp3'
		sp.Popen(['vlc',path])
		return "Playing"
'''

@app.route("/song")
def song():
    return render_template('song_form.html')

@app.route("/playsong/",methods=['GET','POST'])
def playSong():
	if request.method == 'POST':
		id = request.form['song_id']
		path = 'media/'+id+'.mp3'
		sp.Popen(['vlc',path])
		return "Playing"


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)