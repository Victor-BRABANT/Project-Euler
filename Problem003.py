import sys

number = 600_851_475_143

if (len(sys.argv) > 1):
	try:
		number = int(sys.argv[1])
	except:
		pass

max_prime_factor = -1

i = 2
while (i*i <= number):
	while (number % i == 0):	
		max_prime_factor = i
		number = number // i
	i += 1

if (number > 1):
	max_prime_factor = number

print(max_prime_factor)