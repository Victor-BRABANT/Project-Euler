import sys

n = 1000

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass

res = 2**n
res_str = str(res)

somme = 0

for i in res_str:
	somme += int(i)

print(somme)