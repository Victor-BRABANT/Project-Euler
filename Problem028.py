summ = 0

i = 1
jump = 0
corners = 3

while (i <= 1001*1001):
	summ += i
	corners += 1
	if (corners == 4):
		corners = 0
		jump += 2
	i += jump

print(summ)