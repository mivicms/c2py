#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# 用牛顿迭代法 求方程 2*x*x*x-4*x*x+3*x-6 的根

# /* 牛顿迭代法 */

#include 
#include 
# int main()
# {
# double x = 1,x2;
# do {
# x2 = x;
# x -= (2*x*x*x-4*x*x+3*x-6)/(6*x*x-8*x+3);
# } while(fabs(x - x2) > 1e-6);
# printf("root=%.2f\n",x);
# }

def main():
	x=1
	x2 = 0
	while (math.fabs(x - x2) > 1e-6):
		x2 = x
		x-=(2*x*x*x-4*x*x+3*x-6)/(6*x*x-8*x+3)
	print("root=%.2f\n"%x)

main()