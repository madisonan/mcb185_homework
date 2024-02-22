# author: Madison An

# finds the closest color based on R, G, B values

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

dmin = 255*3
color = 'x'
with open(colorfile) as fp:
	for line in fp:
		word = line.split()
		num = word[2].split(',')
		d = abs(int(num[0]) - R) + abs(int(num[1]) - G) + abs(int(num[2]) - B)
		if d < dmin: 
			dmin = d
			color = word[0]
	print(color)
