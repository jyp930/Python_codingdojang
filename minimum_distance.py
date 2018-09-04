import random, sys
n = int(input())
li = random.sample(range(1,50), n)
li.sort()
print(li)
storage_dist = sys.maxsize
storage_pair = []

for i in range(n-1):
	if(li[i+1]-li[i]<storage_dist):
		storage_dist = li[i+1]-li[i]
		storage_pair=[]
		storage_pair.append(tuple((li[i], li[i+1])))
	elif(li[i+1]-li[i]==storage_dist):
		storage_pair.append(tuple((li[i], li[i+1])))

print(storage_pair)