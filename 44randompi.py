#author: Madison An

#Monte Carlo estimate for value of pi
#have to manually stop program 

import random
import math

total = 0
circle = 0
while True:
	total = total + 1
	x = random.random()
	y = random.random()
	distance = math.sqrt(x**2 + y**2)
	if distance < 1:
		circle += 1
	pi = 4 * (circle / total)
	print(pi)