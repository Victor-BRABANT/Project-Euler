import sys

n = 100

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass


sum_squares = 0
square_sum = 0


for i in range(n+1):
	sum_squares += i*i
	square_sum += i

square_sum = square_sum*square_sum

print(square_sum - sum_squares)