# author: Madison An


# this function finds the accuracy and F1 score
def accuracy(tp, fp, tn, fn):
	a = (tp + tn) / (tp + fp + tn + fn)
	if tp == 0:
		return 'error: tp must be greater than 0 for F1 score'
	else:
		r = tp / (tp + fn)
		p = tp / (tp + fp)
		f = 2 * ((p * r) / (p + r))
	return a, f1


# testing
print(accuracy(0, 4, 8, 2))
print(accuracy(5, 9, 2, 5))
print(accuracy(7, 5, 2, 9))