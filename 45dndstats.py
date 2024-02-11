#author: Madison An

import random

rolls = 1000


#3D6
total_scores = 0
for i in range(rolls):
	stat = 0
	for j in range(3):
		d = random.randint(1, 6)
		stat += d
	total_scores += stat
print('avg 3D6 stat:\t', total_scores / rolls)
	

#3D6r1
total_scores = 0
for i in range(rolls):
	stat = 0
	for j in range(3):
		d = random.randint(1, 6)
		if d == 1:
			rd = random.randint(1, 6)
			stat += rd
		else:
			stat += d
	total_scores += stat
print('avg 3D6r1 stat:\t', total_scores / rolls)


#3D6x2
total_scores = 0
for i in range(rolls):
	stat = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2:
			stat += d1
		else:
			stat += d2
	total_scores += stat
print('avg 3D6x2 stat:\t', total_scores / rolls)


#4D6d1
total_scores = 0
for i in range(rolls):
	stat = 0
	for i in range(1):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		d3 = random.randint(1, 6)
		d4 = random.randint(1, 6)
		if d4 <= d1 and d4 <= d2 and d4 <= d3:
			stat = d1 + d2 + d3
		if d3 <= d1 and d3 <= d2 and d3 <= d4:
			stat = d1 + d2 + d4
		if d2 <= d1 and d2 <= d3 and d2 <= d4:
			stat = d1 + d3 + d4
		if d1 <= d2 and d1 <= d3 and d1 <= d4:
			stat = d2 + d3 + d4
	total_scores += stat
print('avg 4D6d1 stat:\t', total_scores / rolls)
