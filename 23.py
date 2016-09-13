#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
import math
for i in range(100000):
    #转化为整型值
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if(x * x == i + 100) and (y * y == i + 268):
        print i