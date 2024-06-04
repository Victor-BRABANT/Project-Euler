import sys
from math import factorial

n = 20

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass

print(factorial(2*n)//(factorial(n)*factorial(n)))