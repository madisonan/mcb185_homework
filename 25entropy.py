# author: Madison An


# this function finds the Shannon entropy for given nucleotide counts
import math
def entropy(a, c, g, t):
	
	# frequency of nucleotide/total
	total = (a + c + g + t)
	xa = a / total
	xc = c / total
	xg = g / total
	xt = t / total
	
	if   a != 0: ha = xa * math.log2(1 / xa)
	elif a == 0: ha = 0
	
	if   c != 0: hc = xc * math.log2(1 / xc)
	elif c == 0: hc = 0
	
	if   g != 0: hg = xg * math.log2(1 / xg)
	elif g == 0: hg = 0
	
	if   t != 0: ht = xt * math.log2(1 / xt)
	elif t == 0: xt = 0
	
	return ha + hc + hg + ht


# testing
print('entropy 1:', entropy(2, 5, 5, 2))
print('entropy 1:', entropy(3, 6, 2, 9))
print('entropy 1:', entropy(7, 2, 0, 5))