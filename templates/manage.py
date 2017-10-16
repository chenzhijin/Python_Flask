#encoding:utf-8

#该文件是加载命令行操作的
from flask_script import Manager      #加载命令操作
from flak_script_demo import app		#加载主程序app
from exts import db						#加载数据库
from db_scripts import DBmanager		#加载数据库命令，因为数据库的命令放在了一个文件里
from flask_migrate import Migrate,MigrateCommand		#加载数据库迁移操作


manager = Manager(app)

@manager.command
def runserver():
	print ('服务器跑起来了！！！')

#和数据库相关的操作都放在一起,建立db_scripts文件
#命令python2 manager.py db init/migrate
manager.add_command('db',DBmanager)

#1.要使用flask_migrate,必须绑定app和db
migrate = Migrate(app,db)

#2.把MigrateCommand添加到manager中
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
	manager.run()

