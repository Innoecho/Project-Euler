import math

def isPrime(x):
	factor = round(math.sqrt(x))
	while factor>1:
		if x%factor == 0:
			return False
		factor-=1
	return True
temp = n = 600851475143
while 1:
	a = int(math.sqrt(temp))
	for x in [2]+range(3,a+1,2):
		if temp%x == 0:
			break
	if temp%x != 0:
		print temp,'=',n
		break
	temp /= x
	print x,'*',
	
