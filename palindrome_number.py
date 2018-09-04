def is_palindrome(n):
	n = str(n)
	for i in range(0,int(len(n)/2)):
		if(n[i]!=n[-1-i]): return False
	return True

stri = '8972798'
print(stri[::-1])

print(is_palindrome(1))

n = int(input())
hit = 0
number = 0
while(True):
	if is_palindrome(number):
		hit+=1
		if(n==hit): break
	number+=1

print(number)
