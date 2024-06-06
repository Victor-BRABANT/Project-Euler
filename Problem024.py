numbers = ['0','1','2','3','4','5','6','7','8','9']

def get_perms(numbers):
	if (len(numbers) == 1):
		return numbers

	permuts = []

	for i in range(len(numbers)):
		numbers_c = numbers.copy()
		prefix = numbers_c[i]
		numbers_c.pop(i)
		perms = get_perms(numbers_c)
		permuts += [prefix + sub for sub in perms]

	return permuts


permutations = get_perms(numbers)
permutations.sort()

print(permutations[999999])