#encoding:utf-8
from flask import Flask
from exts import db
import config
from models import Article	#新建一个article模型，采用models分开的方式

app= Flask(__name__)
app.config.from_object(config)
#数据库加载app,因为无用户访问服务器，app并没有放入栈中
db.init_app(app)
#所以就手动把app推入栈中（很多app是指定app）
with app.app_context():
	db.create_all()

@app.route('/')
def index():
	return 'index'

if __name__=='__main__':
	app.run(debug=True)


