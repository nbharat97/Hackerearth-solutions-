def breakingRecords(scores):
	highest = lowest = 0
	for i in range(0,len(scores)-1):
		if(scores(i)<scores(i+1)):
			highest = highest + 1
		else:
			lowest = lowest + 1
	print (highest+''+lowest)


n = int(raw_input())
scores = []
for i in range(0,n):
	scores.append(input())

breakingRecords(scores)

