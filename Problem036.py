limit = 1_000_000

def is_palindrome(n):
	sn = str(n)
	for i in range(int(len(sn)/2)):
		if sn[i] != sn[len(sn)-i-1]:
			return False
	return True

def to_binary(n):
	bn = ""
	while n > 0:
		bn = str(n%2) + bn
		n = n//2
	return bn

total = 0

for i in range(1,limit+1):
	if is_palindrome(i) and is_palindrome(to_binary(i)):
		total += i

print(total)