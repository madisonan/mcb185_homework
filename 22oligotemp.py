# author: Madison An


# this function finds the melting point of an oligo
def oligo_temp(a, c, g, t):
	if a + c + g + t <= 13:
		mp = (a + t) * 2 + (g + c) * 4
	else:
		mp = 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)
	return mp


# testing
print('melting point 1:', oligo_temp(2, 4, 5, 3))
print('melting piont 2:', oligo_temp(5, 3, 7, 2))
print('melting point 3:', oligo_temp(5, 2, 9, 3))