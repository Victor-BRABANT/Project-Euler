p = 4
nb_max = 0
p_max = 0

def is_rectangular(a,b,c):
	return a*a + b*b == c*c

while p <= 1000:
	possibilities = 0

	for i in range(1, p-2):
		for j in range(i, p-i-2):
			if is_rectangular(i, j, p-i-j):
				possibilities += 1

	if possibilities > nb_max:
		print(p, possibilities)
		nb_max = possibilities
		p_max = p

	p += 1

print(p_max)