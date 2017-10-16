#encoding=utf8
import re

#re.match从头开始匹配符合的字符(串），然后才能返回，第一个元素不符就匹配不成功
ma = re.match(r'[\w+]{6,10}@(163|126).com','1234df@163.com')
mb = re.match(r'{.}','{a}')	#一个点.代表只能匹配一个数字，有{}限制，{ab}报错
mc = re.match(r'..','23hf')
md = re.match(r'[abc]+','azc')		#c不能匹配上
me = re.match(r'[a-z]','o213e')
mf = re.match(r'\[[\w]\]','[d]')	#[]括号需转义
mh = re.match(r'[A-Z]?[a-z]+[1-9]*','Agdgs12')
mi = re.match(r'^[\w]{4,10}@163.com$','immoc@163.com')
mj = re.match(r'\Aimmoc[\w]*|[1-9]','immocpython')
mk = re.match(r'<([\w]+>)[\w]+</\1','<book>python</book>')
ml = re.match(r'<(?P<mark>[\w]+>)[\w]+</(?P=mark)','<book>python</book>')

#re.search()也是从头开始匹配符合的字符(串），但它是整个字符串有符合的就返回，而且只返回第一个符合的字符串
mq = re.search(r'<a src=\w+>\w+</a>','<head>fhiwhf<a src=fiana>nfjdi</a>')

#re.findall()也是从头开始匹配符合的字符(串）,但它遍历整个字符串，符合的值全部组成列表返回,不用group()
mr = re.findall(r'[1-9]','f14jfdis556fsj234')

#re.sub()用来一个字符串或者函数来替换匹配到的字符串
str1 = 'immoc videonum = 1000'
mm = re.sub(r'\d+','1001',str1)
def add1(match):
	val = match.group()
	num = int(val)+10
	return str(num)
mo = re.sub(r'\d+',add1,str1)

#re.spilt()表示去掉匹配上的字符串，分割成列表元素，最后返回list
str2 = 'imoc:C C++ Java Python,Js'
mp = re.split(r':| |,',str2)

print (ma.group())
print (mb.group())
print (mc.group())
print (md.group())
print (me.group())
print (mf.group())
print (mh.group())
print (mi.group())
print (mj.group())
print (mk.group())
print (ml.group())
print (mq.group())
print (mr)
print (mm,'',mo,'\n',mp)

import io
print (io.DEFAULT_BUFFER_SIZE)



import mysql.connector
# 注意把password设为你的root口令:
onn = mysql.connector.connect(user='root', password='password', database='test', use_unicode=True)
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount
1
# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
values
[(u'1', u'Michael')]
# 关闭Cursor和Connection:
cursor.close()
True
conn.close()