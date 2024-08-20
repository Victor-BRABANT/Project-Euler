limit = 1_000_000

def is_prime(n):
	i = 2
	while i < n:
		if n%i == 0:
			return False
		i += 1
	return True


def rotations(n):
	sn = str(n)
	rotations_list = []
	snn = sn+sn
	length = len(sn)
	for i in range(length):
		rotations_list.append(snn[i:i+length])
	return rotations_list

prime_numbers = []

def is_prime_circular(n):
	rotations_list = rotations(n)
	for i in rotations_list:
		i_int = int(i)
		if not i_int in prime_numbers:
			return False
	return True



i = 2
count = 0

while i <= limit:
	if i%10000 == 0:
		print(i)
	is_primee = True
	for k in prime_numbers:
		if (i % k == 0):
			is_primee = False
			break
	if (is_primee):
		prime_numbers.append(i)
	i += 1

for i in prime_numbers:
	if is_prime_circular(i):
		count += 1
	i += 1

print(count)
