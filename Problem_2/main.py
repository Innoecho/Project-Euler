Fib = [1, 2]
while Fib[-1] < 4000000:
	Fib.append(Fib[-1] + Fib[-2])
Fib_even = [x for x in Fib if x%2==0]
print sum(Fib_even)