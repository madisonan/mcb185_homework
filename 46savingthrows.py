#author: Madison An

import random

#normal roll
def roll_normal():
	rn = random.randint(1, 20)
	return rn

#roll with an advantage
def roll_advantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		return r1
	else:
		return r2

#roll with a disadvantage
def roll_disadvantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 <= r2:
		return r1
	else:
		return r2

#probability of successful rolls in each DC
trials = 1000
print('DC \tnorm \t adv \t dis')

for dc in range(5, 16, 5):
	print(dc, end = '\t')
	successnorm = 0
	successadv = 0
	successdis = 0
	for i in range(trials):

		rnnorm = roll_normal()
		if rnnorm >= dc:
			successnorm += 1

		rnadv = roll_advantage()
		if rnadv >= dc:
			successadv += 1

		rndis = roll_disadvantage()
		if rndis >= dc:
			successdis += 1

	print(successnorm / trials,'\t', successadv / trials,'\t', successdis / trials)