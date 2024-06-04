def is_palindrome(n):
	n_str = str(n)
	for i in range(int(len(n_str)/2)):
		if (n_str[i] != n_str[len(n_str)-1-i]):
			return False
	return True

largest = 0

for i in range(100,1000):
	for j in range(100, i+1):
		if (is_palindrome(i*j)):
			if (i*j > largest):
				largest = i*j

print(largest)