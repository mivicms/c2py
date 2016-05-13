#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2

# ＋3.编程找出1000以内的所有完数。

# ___________________________________________________________________

# 程序源代码：

# void main()
# {
# int a=0,i;
# for(i=1;i<1000;i++)
# int j,a=0;
# for(j=1;j<i;j++)
# 	if((i%j)==0)
# 		a+=j;
# 	if(i==a)
# 	printf("%d是完数\n",a);
# return(0);
# }

def main():
	
	for j in range(2,1000):
		a = 0
		for i in range(1,j):
			if j%i==0:
				a+=i
		if j==a:
			print("%d is a wanshu"%j)

main()









