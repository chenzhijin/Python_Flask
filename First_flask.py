#encoding:utf-8
from flask import Flask,url_for,redirect
import config
app = Flask(__name__)
app.config .from_object(config)

#装饰器的作用是做一个URL即网址与视图函数的映射，给函数装上网址，把函数的内容放到网站上去
@app.route('/')
def hello_world():
	#article_url = url_for('article',id= 'abc')#URL反转，由视图函数的名得到其路径即URL
	#return redirect('article_url')	#这是重定向
	return u'这是首页'

@app.route('/article/<id>')
def article(id):
	return '您请求的参数是：%s' %id

@app.route('/login/')
def login():
	return u'这是登录页面'

@app.route('/question/<is_login>/')
def question(is_login):
	if is_login == '1':
		return u'这是发布问答的界面'
	else:
		return redirect(url_for('login'))   #用户没登录时，重定向到登录页面




#如果当前的文件是作为主程序文件，执行app.run()
	#app.run()是用来启动一个应用服务器来接受用户请求的。
		#相当于		while Ture：
					#	listen()
#if __name__=='__main__':
	app.run()