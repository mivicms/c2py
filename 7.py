#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

# 。

# __________________________________________________________________

# 程序分析：利用while语句,条件为输入的字符不为’\n’.

# ___________________________________________________________________

# 程序源代码：

# #include “stdio.h”

# main()

# {char c;

# int letters=0,space=0,digit=0,others=0;

# printf(“please input some characters\n”);

# while((c=getchar())!=’\n’)

# {

# if(c>=’a'&&c<=’z'||c>=’A'&&c<=’Z')

# letters++;

# else if(c==’ ‘)

# space++;

# else if(c>=’0′&&c<=’9′)

# digit++;

# else

# others++;

# }

# printf(“all in all:char=%d space=%d digit=%d others=%

# d\n”,letters,space,digit,others);

# }

def main():
	print("please input some characters\n")
	input = list(raw_input())
	letters = space = digit = others = 0
	for c in input:
		if c !='\n':
			if c>'a' and c<='z' or c>='A' and c<='Z':
				letters += 1
			elif c==' ':
				space += 1
			elif c>'0' and c<='9':
				digit +=1
			else:
				others+=1
	print("all in all:char=%d space=%d digit=%d others=%d\n"%(letters,space,digit,others))

main()