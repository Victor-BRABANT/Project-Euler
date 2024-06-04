import sys
from math import sqrt

n = 500

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass

def number_of_divisors(k):
	number = 2
	for i in range(2, int(sqrt(k))):
		if (k % i == 0):
			number += 2
	return number

triangle_number = 1
i = 2
nb_div = number_of_divisors(triangle_number)


while (nb_div < n):
	triangle_number += i
	i += 1
	nb_div = number_of_divisors(triangle_number)

print(triangle_number)