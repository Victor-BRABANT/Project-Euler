def fact(n):
	if n == 0 or n == 1:
		return 1
	return n*fact(n-1)

total = 0

for i in range(10, 7*fact(9)):
	si = str(i)
	n = len(si)
	summ = 0
	for j in si:
		summ += fact(int(j))
	if summ == i:
		total += i

print(total)