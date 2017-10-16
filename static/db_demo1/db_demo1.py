#encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
#连接数据库
db = SQLAlchemy(app)

#create table article(
#	id int primary key autoincrement,
#	title varchar(100) not null,
#	content text not null,
#)

class Article(db.Model):
	__tablename__ = 'article'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	title = db.Column(db.String(100),nullable=False)
	content = db.Column(db.Text,nullable=False)

db.create_all()

#增删改都要用db.session.xxx(对象）来实习
@app.route('/')
def index():
	#增
	article1 = Article(title='aaa',content='bbb')
	db.session.add(article1)
	#事务
	db.session.commit()

	#查 用到类.query.filter(查询条件)，返回query队列
	# select * from article where title='aaa';
	#result = Article.query.filter(Article.title == 'aaa')[0]
	#article1 = Article.query.filter(Article.title == 'aaa').first()
	#print'title:%s' % article1.title
	#print (result)

	#改：查出来后直接赋值
	#article1 = Article.query.filter(Article.title == 'aaa').first()
	#article1.title = 'new title'
	#db.session.commit()
	#删：查出来后删掉
	article1 = Article.query.filter(Article.content == 'bbb').first()
	db.session.delete(article1)
	db.session.commit()
	return 'index'

if __name__=='__main__':
	app.run(debug=True)