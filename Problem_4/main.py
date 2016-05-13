#coding=utf-8

# 生成给定范围内所有数的列表
numlist = range(10**(3-1),10**3)
maxnum = 0
# 对其中所有元素遍历
for i in numlist:
	for j in numlist:
		k = i*j
		s = str(k)
		# 如果是回文数并且最大，保存
		if s == s[::-1] and k > maxnum:
			maxnum = k
print maxnum

