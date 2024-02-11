import random

#random.randint will include the upper number in the range, so it uses 6
for i in range(3):
	random.randint(1, 6)

#normal distribution function, arguments are mean and standard deviation
for i in range(5):
	print(random.gauss(0.0, 1.0))

#\t separates values with tabs. these line up with each other
print(10, 20, 30, 40, sep='\t')
print(100, 2000, 30000, 40000, sep='\t')

#f-strings make it so variables in curly brackets dump their contents/what it's equal to
i = 1
pi = 3.14159
print('normal string {i} {pi}')
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')
#.3f in the pi is saying to print to 3 digits of precision which does three decimal places
print(f'formatted string {i} {pi:.3f}')

#sys.stderr separates data from message about running time in print statement
import sys
print('logging', file=sys.stderr)
#if redirect program to something else,
#the program output goes to that redirected location
#but the 'logging' is the stderr statement so it prints in terminal still

#pseudorandom
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

#compound assignment
#add increment to old value, can change the num after += to any val want to increase by
a = 2
a += 1
print(a)
#same concept by subtracting
a -= 1
print(a)
#same concept but multiply and assigning
a *= 3
print(a)