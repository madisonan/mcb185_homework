#author: Madison An

#first 10 numbers of fibonacci sequence
def fibonacci(n):
	a = 0
	b = 1
	print(a)
	for i in range(n-2):
		fib = a + b		#sum of two previous values
		print(fib)
		b = a			#b becomes previous number
		a = fib			#then a becomes new number
print(fibonacci(10))