name_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def number_to_name(n):
	if (n == 0):
		return ""
	if (n < 21):
		return name_list[n-1]
	if (n < 100):
		dec = n//10
		dec_name = name_list[19+dec-2]
		unit = n%10
		unit_name = ""
		if (unit != 0):
			unit_name = name_list[unit-1]
		return dec_name+unit_name
	elif (n < 1000):
		cent = n//100
		cent_name = name_list[cent-1] + "hundred"
		rest = n%100
		if (rest != 0):
			rest_name = number_to_name(rest)
			return cent_name+"and"+rest_name
		return cent_name
	else:
		return "onethousand"

count = 0

for i in range(1,1001):
	name = number_to_name(i)
	count += len(name)

print(count)