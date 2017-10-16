#encoding:utf-8
from flask import Flask,session
import os

app = Flask(__name__)
#app.config['SESSION_TYPE'] = 'filesystem'
#app.config.from_object(config)

app.config['SECRET_KET'] = '\xeew\xe4\xc0\xee\xb1]\x9b\xa0\x9e)\x15Qhem\xe5\xf17\xd6\xceB\xb7\xb4'
#添加数据到session中
#操作session的时候，跟操作字典是一样的

@app.route('/')
def index():
	session['username'] = 'zhijin'
	return 'index'

@app.route('/get/')
def get():
	return session.get('username')

@app.route('/get/')
def delete():
	print session.get('username')
	session.pop('username') #session.clear()
	print session.get('username')
	return 'sussess'


if __name__=='__main__':
	app.run(debug=True)