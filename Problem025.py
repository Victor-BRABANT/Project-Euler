a = 1
b = 1
i = 2

while (len(str(b)) != 1000):
	b = a+b
	a = b-a
	i += 1

print(i)

