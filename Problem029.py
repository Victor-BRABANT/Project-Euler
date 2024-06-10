liste = []

for a in range(2,101):
	for b in range(2,101):
		if a**b not in liste:
			liste.append(a**b)

print(len(liste))