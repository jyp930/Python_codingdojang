#vroomfan
total = 0
for i in range(1,10001):
	for ch in str(i):
		if(ch=='8'): total += 1
print(total)

#풀이
print(str(list(range(1,10001))).count('8'))