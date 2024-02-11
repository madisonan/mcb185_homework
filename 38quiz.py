#authors: Jaime Young and Madison An

def gregory(n):
	a = 1
	e = 1
	f = 0
	for pi in range(n):
		pi = 1 + f
		a = a + 2
		e = e * (-1)
		d = e / a
		f = f + d
	return (pi * 4)

print(gregory(100))