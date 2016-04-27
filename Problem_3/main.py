import math
import time

start = time.time()
temp = n = 600851475143
while 1:
	a = int(math.sqrt(temp))
	for x in [2]+range(3,a+1,2):
		if temp%x == 0:
			break
	if temp%x != 0:
		print temp
		break
	temp /= x
print time.time() - start
	
