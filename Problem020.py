from math import factorial

res = factorial(100)
res_str = str(res)

count = 0

for i in res_str:
	count += int(i)

print(count)