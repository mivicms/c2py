#! /usr/bin/python                                                          
# -*- coding: utf-8

# 题目：练习函数调用

# ___________________________________________________________________

# 程序源代码：

# #include <stdio.h>

# void hello_world(void)

# {

# printf(“Hello, world!\n”);

# }

# void three_hellos(void)

# {

# int counter;

# for (counter = 1; counter <= 3; counter++)

# hello_world();/*调用此函数*/

# }

# void main(void)

# {

# three_hellos();/*调用此函数*/

# }

def hello_world():
    print("Hello, world!")
def three_hellos():
    for counter in xrange(1,4):
        hello_world()
        
three_hellos();