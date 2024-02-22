# authors: Madison An and Jaime Young

# birthday simulator but makes a list from the calendar instead

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0
for j in range(trials):
	calendar = []
	for i in range(days):
		calendar.append(0)
	for k in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1
		if calendar[birthday] > 1:
			same += 1
			break
	
print(same / trials)