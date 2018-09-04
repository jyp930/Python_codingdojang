#original
n = int(input())

for i in range(1,n+1):
	if(n%i==0): print((int(n/i),i),end="")
print()

#upgrade
def upgrade_li(li, m):
	if m==1: return li
	else:
		m-=1
		size = len(li)
		for i in range(size):
			temp = li[i]
			#print(li)
			chop_last = divide_2(temp.pop(-1))
			for j in chop_last:
				li.append(temp+j)
				#print(li)
		for i in range(size):
			del li[0]
		return upgrade_li(li, m)


def divide_2(n):
	li = []
	for i in range(1,n+1):
		if(n%i==0): li.append([int(n/i),i])
	return li

def count_divisor(m):
	count = 0
	for i in range(1,m+1):
		if(m%i==0): count+=1
	return count

n,m= input().split(' ')
n=int(n); m=int(m)

li = [[n]]
li = upgrade_li(li, m)

print(li)
