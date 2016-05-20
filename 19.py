#!/usr/bin/env python
# -*- coding: utf-8 -*

# 题目：对10个数进行排序

# ___________________________________________________________________

# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个

# 元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

# 程序源代码：

# #define N 10

# main()

# {int i,j,min,tem,a[N];

# /*input data*/

# printf(“please input ten num:\n”);

# for(i=0;i<N;i++)

# {

# printf(“a[%d]=”,i);

# scanf(“%d”,&a);}

# printf(“\n”);

# for(i=0;i<N;i++)

# printf(“%5d”,a);

# printf(“\n”);

# /*sort ten num*/

# for(i=0;i<N-1;i++)

# {min=i;

# for(j=i+1;j<N;j++)

# if(a[min]>a[j]) min=j;

# tem=a;

# a=a[min];

# a[min]=tem;

# }

# /*output data*/

# printf(“After sorted \n”);

# for(i=0;i<N;i++)

# printf(“%5d”,a);

# }


def main():
	n=10
	print("please input ten num:\n")
	a = raw_input()
	#a = "45 326 22 52 741 63 44 52 154 1"
	a = a.split(" ")
	for i in xrange(0,n):
		print('%5s '%a[i]),
	for i in xrange(0,n):
		min = i
		for j in xrange(i+1,n):
			if int(a[min])>int(a[j]):
				#min = j
				tem = a[j]
				a[j]=a[min]
				a[min] = tem
	print("\nAfter sorted ")
	for i in xrange(0,n):
		print("%5s "%a[i]),

main()




 #define N 10

# main()

# {int i,j,min,tem,a[N];

# /*input data*/



# printf(“\n”);

# for(i=0;i<N;i++)

# printf(“%5d”,a);

# printf(“\n”);

# /*sort ten num*/

# for(i=0;i<N-1;i++)

# {min=i;

# for(j=i+1;j<N;j++)

# if(a[min]>a[j]) min=j;

# tem=a;

# a=a[min];

# a[min]=tem;

# }

# /*output data*/

# printf(“After sorted \n”);

# for(i=0;i<N;i++)

# printf(“%5d”,a);

# }