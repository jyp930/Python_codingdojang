result = list(range(1,5001))

for i in range(1,5001):
	total = i
	for ch in str(i):
		total += int(ch)

	if(total in result): result.remove(total)

print(sum(result))