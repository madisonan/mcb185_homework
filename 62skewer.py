seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10
g = seq[0:w].count('G')
c = seq[0:w].count('C')
for i in range(len(seq) -w):
	lose = seq[i]
	gain = seq[i+w]
	
	if lose == 'C': c -= 1
	elif lose == 'G': g -= 1
	
	if gain == 'C': c+= 1
	elif gain == 'C': g += 1
	
	comp = (c+g)/w
	if (g+c) > 0: skew = (g-c)/(g+c)
	else: skew = 0
	
	print(i, comp, skew)