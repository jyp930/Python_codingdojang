#내꺼
result = {}
for i in range(1,1001):
	for ch in str(i):
		ch = int(ch)
		if(ch in result):
			result[ch] += 1
		else:
			result[ch] = 1

print(result)

print()
#풀이
dic = {i:0 for i in range(0,10)}
for i in range(1,1001):
    for n in str(i):
        dic[int(n)]+=1
print(dic)