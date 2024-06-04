import sys

n = 2_000_000

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass


prime_numbers = [True for i in range(n)]
prime_numbers[0] = False
somme = 0

for i in range(n):
	if (prime_numbers[i]):
		somme += i+1
		k = 1
		while ((i+1)*k <= n):
			prime_numbers[(i+1)*k-1] = False
			k += 1
	i += 1
print(somme)