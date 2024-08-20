def is_pandigital(multiplicand, multiplier, product):
	alls = str(multiplicand)+str(multiplier)+str(product)

	if len(alls) != 9:
		return False

	liste = list(alls)
	liste.sort()

	for i in range(1,10):
		if liste[i-1] != str(i):
			return False

	return True

digits = [1,2,3,4,5,6,7,8,9]
used_products = []
total = 0

for i1 in range(0,9):
	d1 = digits[i1]
	digits.pop(i1)

	for i2 in range(0,8):
		d2 = digits[i2]
		digits.pop(i2)

		for i3 in range(0,7):
			d3 = digits[i3]
			digits.pop(i3)

			for i4 in range(0,6):
				d4 = digits[i4]
				digits.pop(i4)

				for i5 in range(0,5):
					d5 = digits[i5]
					digits.pop(i5)


					prod1 = (d1*10+d2) * (d3*100 + d4*10 + d5)
					prod2 = d1 * (d2*1000 + d3*100 + d4*10 + d5)

					if prod1 not in used_products and is_pandigital(d1*10+d2, d3*100+d4*10+d5, prod1):
						print(str(d1)+str(d2)+' * '+str(d3)+str(d4)+str(d5)+' = '+str(prod1))
						total += prod1
						used_products.append(prod1)

					if prod2 not in used_products and is_pandigital(d1, d2*1000+d3*100+d4*10+d5, prod2):
						print(str(d1)+' * '+str(d2)+str(d3)+str(d4)+str(d5)+' = '+str(prod2))
						total += prod2
						used_products.append(prod2)

					digits.append(d5)
					digits.sort()

				digits.append(d4)
				digits.sort()

			digits.append(d3)
			digits.sort()
	
		digits.append(d2)
		digits.sort()

	digits.append(d1)
	digits.sort()

print(total)
