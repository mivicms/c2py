#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，

# 十位与千位相同。

# ___________________________________________________________________

# 程序分析：同29例

# ___________________________________________________________________

# 程序源代码：

# main( )

# {

# long ge,shi,qian,wan,x;

# scanf(“%ld”,&x);

# wan=x/10000;

# qian=x%10000/1000;

# shi=x%100/10;

# ge=x%10;

# if (ge==wan&&shi==qian)/*个位等于万位并且十位等于千位*/

# printf(“this number is a huiwen\n”);

# else

# printf(“this number is not a huiwen\n”);

# }

def main():
	x = int(raw_input())
	wan = int(x/10000)
	qian = int(x%10000/1000)
	shi = int(x%100/10)
	ge = int(x%10)
	if ge == wan and shi == qian:
		print("this number is a huiwen\n")
	else:
		print("this number is not a huiwen\n")


main()