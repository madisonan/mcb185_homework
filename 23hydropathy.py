# authors: Madison An and Jaime Young


# this function tells the hydrophobicity value of an amino acid
def hydropathy(aa):
	if   aa == 'i': return 4.5
	elif aa == 'v': return 4.2
	elif aa == 'l': return 3.8
	elif aa == 'f': return 2.8
	elif aa == 'c': return 2.5
	elif aa == 'm': return 1.9
	elif aa == 'a': return 1.8
	elif aa == 'g': return -0.4
	elif aa == 't': return -0.7
	elif aa == 's': return -0.8
	elif aa == 'w': return -0.9
	elif aa == 'y': return -1.3
	elif aa == 'p': return -1.6
	elif aa == 'h': return -3.2
	elif aa == 'e': return -3.5
	elif aa == 'q': return -3.5
	elif aa == 'd': return -3.5
	elif aa == 'n': return -3.5
	elif aa == 'k': return -3.9
	elif aa == 'r': return -4.5
	else: return 'not an amino acid'

# testing		
print(hydropathy('i'))
print(hydropathy('t'))
print(hydropathy('b'))