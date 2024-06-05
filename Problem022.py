file = open("0022_names.txt", "r")
liste = file.readline().split(",")

for i in range(len(liste)):
	liste[i] = liste[i].replace('"', "")

liste.sort()

alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0

for i in range(len(liste)):
	score = 0
	for lettre in liste[i]:
		score += alph.index(lettre)+1
	count += score*(i+1)

print(count)