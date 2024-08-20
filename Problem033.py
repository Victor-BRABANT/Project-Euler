def is_non_trivial(n1, n2):
	if n1/n2 >= 1:
		return False
	sn1 = str(n1)
	sn2 = str(n2)
	if sn1[0] == sn2[0]:
		if n1/n2 == int(sn1[1])/int(sn2[1]):
			return True
	elif sn1[0] == sn2[1]:
		if n1/n2 == int(sn1[1])/int(sn2[0]):
			return True
	elif sn1[1] == sn2[1]:
		if n1/n2 == int(sn1[0])/int(sn2[0]):
			return True
	elif sn1[1] == sn2[0]:
		if n1/n2 == int(sn1[0])/int(sn2[1]):
			return True

prod_num = 1
prod_denom = 1

for i1 in range(1,10):
	for i2 in range(1,10):
		for i3 in range(1,10):
			for i4 in range(1,10):
				if is_non_trivial(i1*10+i2, i3*10+i4):
					prod_num *= i1*10+i2
					prod_denom *= i3*10+i4

gcd = 1
i = 1
while i <= min(prod_num, prod_denom):
	if prod_num%i == 0 and prod_denom%i == 0:
		gcd = i
	i += 1

print(prod_denom/gcd)