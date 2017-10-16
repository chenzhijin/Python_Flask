#encoding:utf-8
from flask import g

def login_log():
	print u'用户名：%s' % g.username

def login_ip(ip):
	pass