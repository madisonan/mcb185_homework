#authors: Madison An and Jaime Young

import random

#simulate death saves and keep track of dies, stabilizes, and revives
rolls = 100000

games = 0			#total of ended scenarios
stable = 0			#total of scenarios ending in stable
die = 0				#total of scenarios ending in die
revived = 0			#total of scenarios ending in revived

scs_tot = 0			#total of success rolls
fail_tot = 0		#total of failure rolls
for i in range(rolls):
	success = 0
	failure = 0
	revival = 0
	for j in range(1):
		d = random.randint(1, 20)
		if d == 20:
			revival += 1
			games += 1
		elif d == 1:
			failure += 2
		elif d < 10:
			failure += 1
		else:
			success += 1
	
	scs_tot += success
	fail_tot += failure
	revived += revival
	
	if scs_tot % 3 == 0 and success > 0:
		stable += 1
		games += 1
	if fail_tot % 3 == 0 and failure > 0:
		die += 1
		games += 1

print('probability of stabilizing:', stable / games)
print('probability of dying:', die / games)
print('probability of reviving:', revived / games)