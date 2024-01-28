# author: Madison An


# this function solves the quadratic formula
import math
def quadratic_formula(a, b, c):
	if b**2 - 4 * a * c < 0:
		return 'no real solution'
	elif b**2 - 4 * a * c == 0:
		x = ((-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a)
		return x
	else:
		x1 = ((-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a)
		x2 = ((-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a)
	return x1, x2


# testing
print(quadratic_formula(2, 8, 5))
print(quadratic_formula(6, 2, 3))
print(quadratic_formula(1, 2, 1))