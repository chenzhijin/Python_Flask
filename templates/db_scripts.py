#encoding:utf-8
#命令行操作用Manager
from flask_script import Manager

#创建一个Manager对象
DBmanager = Manager()

#用@Manager对象.command把init修饰成命令
@DBmanager.command
def init():
	print '数据库初始化完成'

@DBmanager.command
def migrate():
	print '数据表迁移成功'