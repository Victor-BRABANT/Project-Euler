from math import sqrt

def is_prime(n):
	if n <= 1:
		return False
	for k in range(2,int(sqrt(n))+1):
		if n%k == 0:
			return False
	return True

max_coef = 0
max_leng = 0

for a in range(-999,1000):
	for b in range(-999,1000):
		n = 0
		leng = 0
		while (is_prime(n*n + a*n + b)):
			n += 1
			leng += 1
		if leng > max_leng:
			max_leng = leng
			max_coef = a*b

print(max_coef)