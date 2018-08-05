# -*- encoding=utf-8 -*-
from db_models import *
from datetime import datetime
from playhouse.shortcuts import model_to_dict,dict_to_model

# 链接数据库
database.connect()

# 创建表
# database.create_tables([User,Tweet])

# 向表中添加数据
# User.create(username = 'Katy Perry')
# User.create(username = 'Holsey')
# User.create(username = 'Taylor')
# User.create(username = 'Puth')
# User.create(username = 'Adele').save()

# 向表2中添加数据
user = User.create(username = 'Obama')
u = model_to_dict(user)
print u

# user_data = {'id':17,'username':'Obama'}
# user = dict_to_model(User,user_data)
# print user.username
# Tweet.create(user_id = 11 ,message = 'Winter coming!')

# 查询数据
# print User.get(User.username == 'Holsey')

# usernames = ['Katy Perry','Holsey','Taylor','Puth','Adele']

# users  = User.select().where(User.username << usernames)

# tweets = Tweet.select().where(Tweet.user << users)

# for i in users:

#     print i.username

# get方法只能查询到一条数据
t = Tweet.get(message = 'This is a field')
print t.user_id,t.created_date,t.is_published

# 使用filter方法可以查询多条数据
ts = Tweet.filter(user_id = 11)
for i in ts:
    print i.message

# 查询表内容

# for i in New.select():
#     print i,i.age,i.name,i.location,i.com
    # print i._dict_


# 插入新的行数
# New.create(age=30,name='huangxiafei',location='shantou')





























