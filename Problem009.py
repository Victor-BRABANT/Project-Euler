a = 1
b = 2
c = 3

while True:
	if (a*a + b*b == c*c):
		if (a+b+c == 1000):
			break

	if (a+1 == b):
		if (b+1 == c):
			c += 1
			b = 2
		else:
			b += 1
		a = 1
	else:
		a += 1

print(a*b*c)