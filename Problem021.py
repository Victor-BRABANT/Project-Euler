from math import sqrt

def sum_of_div(n):
	somme = 0

	for i in range(1, int(sqrt(n))+1):
		if (n%i == 0):
			somme += i
			somme += int(n/i)

	return somme-n

def is_amicable(n):
	s = sum_of_div(n)
	return n == sum_of_div(s) and n != s

tot = 0

for i in range(1, 10000):
	if is_amicable(i):
		tot += i

print(tot)