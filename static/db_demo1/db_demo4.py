#encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
#连接数据库
db = SQLAlchemy(app)

#关联表的创建是用db.Table(表id,db.Column(列id，类型，引用的外键，..)来创建对象的
article_tag = db.Table(
	'article_tag',#\
	db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
	db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True)
)

class Article(db.Model):
	__tablename__ = 'article'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	title = db.Column(db.String(100),nullable=False)
	content = db.Column(db.Text,nullable=False)
	#secondary是中间表的意思
	tags = db.relationship('Tag',secondary=article_tag,backref=db.backref('articles'))

class Tag(db.Model):
	__tablename__ = 'tag'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/')
def index():
	article1 = Article(title='aaa',content='c1')
	article2 = Article(title='bbb',content='c2')

	tag1 = Tag(name='111')
	tag2 = Tag(name='222')

	#在中间表中用两个表的关联再加append增加数据
	article1.tags.append(tag1)
	article1.tags.append(tag2)

	article2.tags.append(tag1)
	article2.tags.append(tag2)

	db.session.add(tag1)
	db.session.add(tag2)

	db.session.add(article1)
	db.session.add(article2)

	db.session.commit()

	article3 = Article.query.filter(Article.title == 'aaa').first()
	tags= article3.tags
	for tag in tags:
		print tag.name

	return 'index'

if __name__=='__main__':
	app.run(debug=True)