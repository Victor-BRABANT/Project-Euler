from math import sqrt

abudants = []
numbers = [False for i in range(28123)]


for i in range(28123):
	somme = 0
	for j in range(1,int(sqrt(i))+1):
		if (i%j == 0):
			somme += j
			if (int(i/j) != j):
				somme += int(i/j)
	somme -= i
	if (somme > i):
		abudants.append(i)

for i in range(len(abudants)):
	for j in range(i, len(abudants)):
		a = abudants[i]
		b = abudants[j]
		if (a+b >= 28123):
			break
		numbers[a+b] = True

somme = 0

for i in range(len(numbers)):
	if (not numbers[i]):
		somme += i

print(somme)