numlist = range(10**(3-1),10**3)
maxnum = 0

for i in numlist:
	for j in numlist:
		k = i*j
		templist = list(str(k))
		templist.reverse()
		tempstr = ''
		for c in templist:
			tempstr += c
		kk = int(tempstr)
		if k == kk and k > maxnum:
			maxnum = k
print maxnum

