import sys

max_value = 4_000_000

if (len(sys.argv) > 1):
	try:
		max_value = int(sys.argv[1])
	except:
		pass

last_fib_value = 1
fib_value = 2

total = 0

while (fib_value < max_value):
	if (fib_value % 2 == 0):
		total += fib_value
	fib_value = fib_value + last_fib_value
	last_fib_value = fib_value - last_fib_value

print(total)