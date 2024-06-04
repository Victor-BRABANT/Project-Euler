import sys

n = 20

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass

number = 0

not_found = True

while not_found:
	number += 1
	not_found = False
	for i in range(1,n+1):
		if (number % i != 0):
			not_found = True
			break
	

print(number)