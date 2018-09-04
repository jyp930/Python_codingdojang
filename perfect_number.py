def perfect_number(n):
	total = 0
	for j in range(1,n):
		if(n%j==0): total += j
	if(n==total): return True
	else: return False

n = int(input())
for i in range(1,n+1):
	if(perfect_number(i)): print(i, end=" ")
print()