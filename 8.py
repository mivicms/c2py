#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如

# 2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

# __________________________________________________________________

# 程序分析：关键是计算出每一项的值。

# ___________________________________________________________________

# 程序源代码：

# main()

# {

# int a,n,count=1;

# long int sn=0,tn=0;

# printf(“please input a and n\n”);

# scanf(“%d,%d”,&a,&n);

# printf(“a=%d,n=%d\n”,a,n);

# while(count<=n)

# {

# tn=tn+a;

# sn=sn+tn;

# a=a*10;

# ++count;

# }

# printf(“a+aa+…=%ld\n”,sn);

# }


def main():
	sn = tn = 0
	count = 1
	print("please input a and n\n")
	s = raw_input()
	a,n = s.split(' ')
	print("a=%s,n=%s\n"%(a,n))
	while (count<=int(n)):
		tn = tn+int(a)
		sn = sn+tn
		a = int(a)*10
		count +=1
	print("a+aa+aaa+...=%s\n"%sn)

main()