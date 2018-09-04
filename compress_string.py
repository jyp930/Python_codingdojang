string = input()
result = ""
count = 0; memory = ''

for i in string:
	if(count==0):
		result += i
		count += 1; memory=i
	else:
		if(i == memory): count+=1
		else:
			result += str(count)
			result += i
			count=1; memory=i
result+=str(count)

print(result)