
# -*- coding: UTF-8 -*-
import time
from datetime import datetime

# 显示当前的时间点
time_stct = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 2018-08-04 10:29:04

# 显示当前时间戳
timestamp = int(time.time())

timeArray = time.localtime(timestamp)  # 将时间戳变为时间元祖

nowtime = time.strftime('%Y-%m-%d %H:%M:%S',timeArray)

print time_stct
print timestamp
print timeArray
print nowtime

#*********************************************************************
# 将字符串时间变成时间戳或者时间类型
time_str = '2018-08-04 10:29:04'

tm = time.strptime(time_str,'%Y-%m-%d %H:%M:%S')  # 将字符串变成时间元祖

time_Stamp = int(time.mktime(tm))

print tm
print time_Stamp








