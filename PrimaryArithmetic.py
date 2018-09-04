while(True):
	num_1, num_2 = input().split(' ')
	if(num_1 == '0' and num_2 == '0'):
		break

	if len(num_2)>len(num_1): num_1, num_2 = num_2, num_1 #더 긴게 num_1
	carry_count = 0
	carry = 0
	
	for i in range(len(num_1)):
		if i < len(num_2):
			if(int(num_1[-(i+1)])+int(num_2[-(i+1)])+carry >= 10):
				carry_count += 1
				carry = 1
			else: carry = 0
		else:
			if(int(num_1[-(i+1)])+carry >= 10):
				carry_count += 1
				carry = 1
			else: carry = 0

	if carry_count == 0: print("No carry operation.")
	else: print("%d carry operation" % carry_count)