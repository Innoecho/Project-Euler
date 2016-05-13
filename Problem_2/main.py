#coding=utf-8
#计算小于4000000的斐波那契数列
Fib = [1, 2]
while Fib[-1] < 4000000:
	Fib.append(Fib[-1] + Fib[-2])
#求数列中所有的奇元素
Fib_even = [x for x in Fib if x%2==0]
求奇元素和
print sum(Fib_even)