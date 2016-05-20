#!/usr/bin/env python
# -*- coding: utf-8 -*

# 题目：求一个3*3矩阵对角线元素之和

# ___________________________________________________________________

# 程序分析：利用双重for循环控制输入二维数组，再将a累加后输出。

# ___________________________________________________________________

# 程序源代码：

# main()
# {
# int x[3][3]={0};
# int a=0,b=0;  //分别是两个对角线和
# int i,j;
# for(i=0;i<3;i++)
# for(j=0;j<3;j++)
# {
# printf("输入%d行%d列数.\n",i,j);
# scanf("%d",&x[i][j]);
# }
# for(i=0;i<3;i++)
# for(j=0;j<3;j++)
# {
# if(i==j) a=a+x[i][j];
# if(i+j==2) b=b+x[i][j];
# }
# printf("a=%d,b=%d\n",a,b,);
# }


def main():
	#x = [[0] * 3] * 3
	x = [[] for i in range(3)]
	a=b=0
	for i in xrange(0,3):
		for j in xrange(0,3):
			print("please input row and col")
			x[i].append(raw_input())
	for i in xrange(0,3):
		for j in xrange(0,3):
			if(i==j):
				a= a+int(x[i][j])
			if(i+j==2):
				b=b+int(x[i][j])
	print("a=%d,b=%d\n"%(a,b))

main()