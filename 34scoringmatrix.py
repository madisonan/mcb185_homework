#authors: Madison An and Jaime Young

n = 'ACGT'
for i in n:
	print('  ', i, sep=' ', end='')
print( )

for nt1 in n:
	print(nt1, end=' ')
	for nt2 in n:
		if nt1 == nt2:
			print('+1', end='  ')
		else:
			print('-1', end='  ')
	print( )