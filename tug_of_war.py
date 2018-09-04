import random

total_case = int(input())
for each_case in range(total_case):
	num_total_people = int(input())
	total_people = []
	for i in range(num_total_people):
		person_weight = int(input())
		total_people.append(person_weight)
	middle = len(total_people)//2
	group1 = total_people[:middle]
	group2 = total_people[middle:]
	count = 0 #충분히 돌린 것 같을 경우 break
	#무작위 교체
	for i in range(100000):
		sum_group1 = sum(group1); sum_group2 = sum(group2)
		sub = abs(sum_group1-sum_group2)
		idx1 = random.randint(0,middle-1)
		idx2 = random.randint(0,len(total_people)-middle-1)

		group1[idx1], group2[idx2] = group2[idx2], group1[idx1]
		if(sub <= abs(sum(group1)-sum(group2))):
			group1[idx1], group2[idx2] = group2[idx2], group1[idx1]
			count += 1
			if(count > middle*100): break #충분히 돌린 것 같을 경우 break
		else:
			count = 0

		if(sum(group1)==sum(group2)): break #같아도 break

	sum_group1 = sum(group1); sum_group2 = sum(group2)
	if(sum_group1>sum_group2):
		print(sum_group2, sum_group1)
	else:
		print(sum_group1, sum_group2)


'''
80
434
253
166
441
102
356
107
144
93
380
387
14
302
330
1
298
262
154
184
362
381
231
76
52
84
115
135
153
129
359
438
131
394
427
213
321
276
256
24
79
175
418
150
415
387
143
38
252
222
326
331
147
78
378
232
17
228
316
360
140
178
301
384
239
78
286
77
385
420
51
88
428
371
217
206
267
133
140
267
25
438
442
10
217
300
127
280
88
149
244
89
330
405
140
149
26
134
384
435
'''