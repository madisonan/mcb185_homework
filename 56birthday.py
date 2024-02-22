# authors: Madison An and Jaime Young

# simulates random birthdays and finds matching birthdays 

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0
for i in range(trials):
	birthdays = []
	for j in range(people):
		day = random.randint(1, days)
		if day in birthdays:
			same += 1
			break
		birthdays.append(day)
	
print(same / trials)