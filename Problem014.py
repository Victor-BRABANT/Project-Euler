import sys

n = 1_000_000

if (len(sys.argv) > 1):
	try:
		n = int(sys.argv[1])
	except:
		pass

seq_leng = [-1 for i in range(n)]

def next_term(k):
	if (k % 2 == 0):
		return k//2
	return 3*k + 1

for i in range(1, n):
	size = 1
	num = i
	while (num != 1):
		num = next_term(num)
		if (num < n and seq_leng[num] != -1):
			size += seq_leng[num]
			num = 1
		else:
			size += 1
	seq_leng[i] = size

print(seq_leng.index(max(seq_leng)))