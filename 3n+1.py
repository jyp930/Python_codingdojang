def maximum_cycle(n, count):
	if n==1: 
		count+=1
		return count
	elif n%2==0:
		count+=1
		return maximum_cycle(n/2, count)
	else:
		count+=1
		return maximum_cycle(3*n+1, count)

first, second = input().split()
first = int(first); second = int(second)
maximum = 0

for i in range(first,second+1):
	temp = maximum_cycle(i,0)
	if(temp > maximum): maximum = temp

print(maximum)