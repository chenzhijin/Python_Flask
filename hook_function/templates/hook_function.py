#encoding:utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'index'

#before_request:请求之前，视图函数之前执行，它只是一个装饰器，可以把钩子函数放到
			#视图函数之前执行
@app.before_request
def my_before_request():
	print 'hello'


if __name__=='__main__':
	app.run(debug=True)