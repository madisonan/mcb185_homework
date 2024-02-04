#author: Madison An

#factorial function and import math
def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac
import math

#poisson probability
def poisson(k, n):
	prob = (n ** k) * (math.e ** (-n)) / factorial(k)
	return prob
	
#testing
print(poisson(3, 6))
print(poisson(8, 12))
print(poisson(14, 17))