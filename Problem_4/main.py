numlist = range(10**(3-1),10**3)
maxnum = 0

for i in numlist:
	for j in numlist:
		k = i*j
		s = str(k)
		if s == s[::-1] and k > maxnum:
			maxnum = k
print maxnum

