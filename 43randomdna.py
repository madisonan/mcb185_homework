#author: Madison An

#makes random DNA sequence with length between 50 - 60

import random

num_of_seq = 3
for i in range(1, num_of_seq+1):
	length = random.randint(50, 60)
	print(f'seq-{i}')
	for j in range(length):
		print(random.choice('ACGT'), end='')
	print()