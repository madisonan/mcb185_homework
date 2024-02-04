#authors: Madison An and Jaime Young

#estimate value of pi using Nilakantha series
def nilakantha(n):
	a = 0
	b = 1
	c = 2
	e = 1
	f = 0
	for pi in range(n):
		pi = 3 + f
		a = a + 2
		b = b + 2
		c = c + 2
		d = e*4 / (a * b * c)
		e = e * (-1)
		f = f + d
	return pi

print(nilakantha(100))