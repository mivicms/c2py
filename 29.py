#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：暂停一秒输出。

import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
	print key, value
	time.sleep(1) # 暂停 1 秒





print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 暂停一秒
time.sleep(1)

print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))