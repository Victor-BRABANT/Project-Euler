total = 0
i = 2
while i <= 354294:
	i_s = str(i)
	somme_puiss = 0
	for c in i_s:
		somme_puiss += int(c)**5
	if somme_puiss == i:
		total += i

	i += 1
print(total)