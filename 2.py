#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：判断101-200之间有多少个素数，并输出所有素数。

# __________________________________________________________________

# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整

# 除，则表明此数不是素数，反之是素数。

# ___________________________________________________________________

# 程序源代码：

# #include “math.h”

# main()

# {

# int m,i,k,h=0,leap=1;

# printf(“\n”);

# for(m=101;m<=200;m++)

# { k=sqrt(m+1);

# for(i=2;i<=k;i++)

# if(m%i==0)

# {leap=0;break;}

# if(leap) {printf(“%-4d”,m);h++;

# if(h%10==0)

# printf(“\n”);

# }

# leap=1;

# }

# printf(“\nThe total is %d”,h);

# }

def main():
	m=i=k=h=0
	leap=1
	for m in range(101,200):
		k = (m+1)**0.5
		for i in range(2,int(k)):
			if m%i == 0:
				leap=0
				break
		if leap:
			print('%s' % m)
			h+=1
			if h%10 == 0:
				print('\n')
		leap=1
	print("\nThe total is %d" % h)


main()