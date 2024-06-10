def update_reste(d,r):
	while (r != 0 and r < d):
		r *= 10
	return r

def cycle_length(d):
	l = 0
	liste = []
	reste = update_reste(d, 1)
	while (reste != 0 and reste not in liste):
		liste.append(reste)
		l += 1
		reste = update_reste(d, reste%d)

	return l

maxi = 0
d_max = 0

for d in range(1,1000):
	print(d)
	leng = cycle_length(d)
	if leng > maxi:
		maxi = leng
		d_max = d

print(d_max)