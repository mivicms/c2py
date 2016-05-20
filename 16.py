#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，

# 则继续判断第二个字母。

# ___________________________________________________________________

# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语

# 句判断第二个字母。

# ___________________________________________________________________

# 程序源代码：

# #include <stdio.h>

# void main()

# {

# char letter;

# printf(“please input the first letter of someday\n”);

# while ((letter=getch())!=’Y') /*当所按字母为Y时才结束*/

# { switch (letter)

# {case ‘S’:printf(“please input second letter\n”);

# if((letter=getch())==’a')

# printf(“saturday\n”);

# else if ((letter=getch())==’u')

# printf(“sunday\n”);

# else printf(“data error\n”);

# break;

# case ‘F’:printf(“friday\n”);break;

# case ‘M’:printf(“monday\n”);break;

# case ‘T’:printf(“please input second letter\n”);

# if((letter=getch())==’u')

# printf(“tuesday\n”);

# else if ((letter=getch())==’h')

# printf(“thursday\n”);

# else printf(“data error\n”);

# break;

# case ‘W’:printf(“wednesday\n”);break;

# default: printf(“data error\n”);

# }

# }

# }

#import os
from sys import stdin 


def main():
	print("please input the first letter of someday\n")

	#letter = char(raw_input())
	letter = stdin.read(1) 
	stdin.flush() 
	if letter != 'Y':
		if letter == 'S':
			print('please input second letter\n')
			letter = stdin.read(1) 
			stdin.flush()
			if letter == 'a':
				print("saturday")
			elif letter == 'u':
				print("sunday")
			else:
				print("data error")
		elif letter == 'F':
			print("friday")
		elif letter == 'M':
			print("monday")
		elif letter == 'T':
			print('please input second letter\n')
			letter = stdin.read(1) 
			stdin.flush()
			if letter == 'u':
				print("tuesday")
			elif letter == 'h':
				print("thursday")
			else:
				print("data error")
		elif letter == 'W':
			print("wednesday")
		else:
			print("data error")

# def main():
# 	print("please input the first letter of someday\n")

# 	#letter = char(raw_input())
# 	letter=os.system("pause")
# 	while letter != 'Y':
# 		if letter == 'S':
# 			print('please input second letter\n')
# 			letter = os.system("pause")
# 			if letter == 'a':
# 				print("saturday")
# 			elif letter == 'u':
# 				print("sunday")
# 			else:
# 				print("data error")
# 		elif letter == 'F':
# 			print("friday")
# 		elif letter == 'M':
# 			print("monday")
# 		elif letter == 'T':
# 			print('please input second letter\n')
# 			letter = os.system("pause")
# 			if letter == 'u':
# 				print("tuesday")
# 			elif letter == 'h':
# 				print("thursday")
# 			else:
# 				print("data error")
# 		elif letter == 'W':
# 			print("wednesday")
# 		else:
# 			print("data error")

main()