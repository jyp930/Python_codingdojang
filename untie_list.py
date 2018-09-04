li = eval(input("중첩리스트를 입력하세요:"))

i = 0
while i<len(li):
	if type(li[i]) == type([]):
		li = li[:i] + li[i] + li[i+1:] 
		i = i-1
	i = i+1

print(li)