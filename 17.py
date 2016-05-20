#!/usr/bin/env python
# -*- coding: utf-8 -*

# 题目：Press any key to change color, do you want to try it. Please

# hurry up!

# ___________________________________________________________________

# 程序源代码：

# #include <conio.h>

# void main(void)

# {

# int color;

# for (color = 0; color < 8; color++)

# {

# textbackground(color); /*设置文本的背景颜色*/

# cprintf(“This is color %d\r\n”, color);

# cprintf(“ress any key to continue\r\n”);

# getch(); /*输入字符看不见*/

# }

# }


class Logger:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	@staticmethod
	def log_normal(info):
		print(Logger.OKBLUE + info + Logger.ENDC)

	@staticmethod
	def log_high(info):
		print(Logger.OKGREEN + info + Logger.ENDC)

	@staticmethod
	def log_fail(info):
		print(Logger.FAIL + info + Logger.ENDC)
	
Logger.log_normal("This is a normal message!")
Logger.log_fail("This is a fail message!")
Logger.log_high("This is a high-light message!")


		