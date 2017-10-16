#encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from exts import db
import config

app = Flask(__name__)
#连接数据库
db.init_app(app)

db = SQLAlchemy(app)

'''create table users(
	id int primary key autoincrement,
	uername varchar(100) not null
)

create table article(
	id int primary keyautocrement,
	title varchat(100) not null,
	conttent text not null,
	author_id int,
	foreign key 'author_id' references 'user.id'
)'''

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer,primary_key = True,autoincrement = True)
	username = db.Column(db.String(100),nullable=False,unique = True)
	#article = db.relationship('Article', backref='users')

class Article(db.Model):
	__tablename__ = 'article'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	title = db.Column(db.String(100),nullable=False)
	content = db.Column(db.Text,nullable=False)
	author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	#db.relation()用来快速关联的函数，article1.author为author_id,从User中找外键，
	author = db.relationship('User',backref=db.backref('articles'))

db.create_all()

@app.route('/')
def index():
	#先创建一个用户
	#user1 = User(username='huashi')
	#db.session.add(user1)
	#db.session.commit()

	#创建文章并且关联用户
	#article1 = Article(title='ddd',content='ccc',author_id=2)
	#db.session.add(article1)
	#db.session.commit()

	#查找作者名
	#article = Article.query.filter(Article.title == 'ddd').first()
	#author_id =article.author_id
	#user = User.query.filter(User.id == author_id).first()
	#print (user.username)

	#运用article.author来给author_id赋值；
	#article1 = Article(title='qffswe',content='wewfqbb')
	#article1.author = User.query.filter(User.id == 1).first()
	#db.session.add(article1)
	#db.session.commit()

	#我要找文章标题为aaa的作者
	#article2 = Article.query.filter(Article.title == 'aaa').first()
	#print 'username:%s' % article2.author.username

	#y运用user.articles来查找该作者写过的所有文章
	user = User.query.filter(User.username == 'huashi').first()
	result = user.articles
	for article3 in result:
		print '-'*10
		print article3.title

	return 'index'

if __name__=='__main__':
	app.run(debug=True)