#encoding:utf-8
#数据库表的修改为了不用每次都删除表再重建，使用flask_migrate数据库迁移模块，它是基于命令行操作的
from flask_script import Manager      #加载命令操作
from migrate_demo import app		#加载主程序app
from exts import db						#加载数据库
from flask_migrate import Migrate,MigrateCommand		#加载数据库迁移操作
from models import Article	#重点是对这个表Article操作,需要修改的都要导入进来

#1.命令python2 manage db init ：建立迁移模块，创建了文件migrations
#2.命令Python2 manage db migrate:迁移修改的数据库表到migrations/vertions中
#3.命令python2 manager db upgrade:迁移的数据库表更新至数据库中

manager =Manager(app)

#1.要使用flask_migrate，必须绑定app和db
migrate = Migrate(app,db)
#2.把MigrateCommand命令添加到manager中
manager.add_command('db',MigrateCommand)

if __name__=='__main__':
	manager.run()