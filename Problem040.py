indexs = [1,10,100,1000,10000,100000,1000000]

i = 1
index = 1
prod = 1


while len(indexs) != 0:
	if index >= indexs[0]:
		si = str(i)
		d = si[len(si)-1-(index-indexs[0])]
		prod *= int(d)
		indexs.pop(0)
	i += 1
	si = str(i)
	index += len(si)

print(prod)
