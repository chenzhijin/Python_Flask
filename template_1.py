#encoding:utf-8

from flask import Flask,url_for,redirect,render_template
import config

#创建一个flask对象，要传进__name__参数
app = Flask(__name__)
#加载配置文件
app.config .from_object(config)

#使用render_template()函数渲染模板index
@app.route('/')
def index():
	#传递参数较多时，使用字典表示，然后再传他们的指针
	context = {
		'username':'陈志金',
		'school':'华南师范大学计算机学院',
		'QQ':'931086794',
		'websites':{
			'baidu':'www.baidu.com',
			'google':'www.google.com'
		}
	}
	return render_template('index.html',**context)	#index放在template文件夹下

@app.route('/<is_login>/')
def login(is_login):
	context = {
		'username': '陈志金',
		'school': '华南师范大学计算机学院',
		'QQ': '931086794',
		'picture': 'http://img0.ph.126.net/BLR2NhbuRDmpmeVRXJTOaw==/1993405785166424238.jpg',
		'websites': {
			'baidu': 'www.baidu.com',
			'google': 'www.google.com'
		}
	}
	if is_login == '1':
		user = {
			'用户': '陈志金',
			"学校": '华师',
			"age" : 19
		}
		return render_template('login.html',**context,user=user)
	else:
		return render_template('index.html',**context)

if __name__ == "__main__":
	app.run()