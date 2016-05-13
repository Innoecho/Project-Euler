#coding=utf-8
import math

temp = n = 600851475143
while 1:
	# 对n作素因子分解
	# 从2到根n搜索
	a = int(math.sqrt(temp))
	for x in [2]+range(3,a+1,2):
		# 找到一个素因子就退出循环
		if temp%x == 0:
			break
	# 如果没有找到，证明n无法被分解，退出
	if temp%x != 0:
		print temp
		break
	# 如果找到，以n/x代替n重新循环
	temp /= x

	
