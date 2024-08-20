list_of_coins = [1,2,5,10,20,50,100,200]

objectif = 200

possibilities = 0

def make_objectif(obj, liste):
	n = len(liste)
	if obj == 0:
		return 1
	if n == 0:
		return 0

	if liste[n-1] <= obj:
		return make_objectif(obj-liste[n-1], liste) + make_objectif(obj, liste[:n-1])

	return make_objectif(obj, liste[:n-1])

print(make_objectif(objectif, list_of_coins))