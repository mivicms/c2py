#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：输入两个正整数m和n，求其最大公约数和最小公倍数。

# __________________________________________________________________

# 程序分析：利用辗除法。

# ___________________________________________________________________

# 程序源代码：

# main()

# {

# int a,b,num1,num2,temp;

# printf(“please input two numbers:\n”);

# scanf(“%d,%d”,&num1,&num2);

# if(num1 　{ temp=num1;

# num1=num2;

# num2=temp;

# }

# a=num1;b=num2;

# while(b!=0)/*利用辗除法，直到b为0为止*/

# {

# temp=a%b;

# a=b;

# b=temp;

# }

# printf(“gongyueshu:%d\n”,a);

# printf(“gongbeishu:%d\n”,num1*num2/a);

# }


def main():
	print("please input two numbers:\n")
	s=raw_input()
	#输入1 2 3
	num1,num2=s.split(' ')
	if num1 > num2:
		temp = int(num1)
		num1 = int(num2)
		num2 = temp
	a=int(num1)
	b = int(num2)
	while (b!=0):
		temp = int(a%b)
		a=b
		b=temp
	print("gongyueshu:%d\n"%a)
	print("gongbeishu:%d\n"%(int(num1)*int(num2)/int(a)))

main()