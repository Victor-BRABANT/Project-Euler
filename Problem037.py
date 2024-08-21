prime_numbers = [2,3,5,7]

def is_prime_truncable(n):
	sn = str(n)
	for i in range(1,len(sn)):
		if not int(sn[i:]) in prime_numbers:
			return False
		if not int(sn[:len(sn)-i]) in prime_numbers:
			return False
	return True



i = 11
count = 0
total = 0

while count < 11:
	if i%10000 == 0:
		print(i)
	is_primee = True
	for k in prime_numbers:
		if k > i:
			break
		if (i % k == 0):
			is_primee = False
			break
	if (is_primee):
		prime_numbers.append(i)
		if is_prime_truncable(i):
			count += 1
			total += i
			print(count, i)

	i += 1

print(total)