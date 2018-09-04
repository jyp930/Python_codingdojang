def is_slump(string):
	#길이
	if(len(string) < 3): return False
	#F 앞부분
	if(string[0] != 'D' and string[0] != 'E'): return False
	if(string[1] != 'F'): return False
	#F부분
	i = 1
	while(string[i] == 'F'):
		i = i+1
		if(i == len(string)): return False
	#F 뒷부분
	if(string[i] == string[-1]): #마지막 문자인 경우
		if(string[i] == 'G'): return True
	else:
		return is_slump(string[i:])
	#위의 경우가 아니면
	return False

def is_slimp(string):
	#길이
	if(len(string) < 2): return False
	if(string[0] != 'A'): return False
	if(len(string) == 2):
		if(string[1] == 'H'): return True
		else: return False
	#두 개의 문자 이상일 때
	if(string[-1] != 'C'): return False
	if(string[1] == 'B'):
		return is_slimp(string[2:-1])
	else:
		return is_slump(string[1:-1])
	#위의 경우가 아니면 
	return False

def is_slurpy(string):
	#길이
	if(len(string) < 5): return False
	i = len(string) - 1
	while(string[i] != 'H' and string[i] != 'C'):
		i = i-1
		if(i<0): return False
	
	result1 = is_slimp(string[:i+1])
	result2 = is_slump(string[i+1:])
	return (result1 and result2)

n = int(input())
print('SLURPYS OUTPUT')
for i in range(n):
	string = input()
	result = is_slurpy(string)
	if(result): print('YES')
	else: print('NO')
print('END OF OUTPUT') 