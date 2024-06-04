import sys

n = 10001

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass


prime_numbers = []
i = 2
founded = 0

while (founded < n):
	is_prime = True
	for k in prime_numbers:
		if (i % k == 0):
			is_prime = False
			break
	if (is_prime):
		prime_numbers.append(i)
		founded += 1
	i += 1

print(prime_numbers[-1])