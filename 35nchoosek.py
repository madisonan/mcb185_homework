#authors: Madison An

#factorial function
def factorial(n):
	if n == 0: return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

#n choose k
def nchoosek(k, n):
	prob = factorial(n) / (factorial(k) * factorial(n - k))
	return prob

#testing
print(nchoosek(4, 8))
print(nchoosek(6, 9))
print(nchoosek(13, 21))