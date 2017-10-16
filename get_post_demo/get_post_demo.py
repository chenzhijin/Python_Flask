#encoding:utf-8
from flask import Flask,render_template,request,g,session,redirect,url_for
from utils import login_log
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search/')
def search():
	print request.args	#获取url的所有参数，字典形式
	print request.args.get('c')		#获取用户提交的参数，GET请求
	return u'用户提交的查询参数是：%s' % request.args.get('c')

#默认的视图函数只采用GET请求，要用POST请求要用到methods
@app.route('/login/',methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username = request.form.get('username')		#获取后台数据
		password = request.form.get('password')
		if username == 'zhijin' and password == 'huashi':
			session['username'] = 'zhijin'
			g.username = 'zhijin'	#g在同一次浏览器的请求中的所有代码均可以使用
			g.password = 'huashi'
			login_log()
			return u'恭喜！登录成功！'
		else:
			return u'你的用户名或者密码错误'

@app.before_request
def my_before_request():
	user_id = session.get('user_id')
	user = User.query.filter(User.id==user_id).first
	if session.get('username'):
		g.username = session.get('username')

@app.route('/edit/')
def edit():
	if session.get('username'):
		return 'hello'
	else:
		return redirect(url_for('login'))

#上下文处理器返回的是一个字典，字典中的key会被模板中的变量来渲染，在所有的页面均可以使用
@app.context_processor
def my_context_processor():
	username = session.get('username')
	if username:
		return {'username':username}

if __name__=='__main__':
	app.run(debug=True)