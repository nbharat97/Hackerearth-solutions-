N = int(input())
count = 0
a = []
for i in range(0,N):
	(a.append(int(input())))
Q = input()
for i in range(0,N):
    if(a[i] == Q):
        print("Present")
        break
    if(i == N):
        print("Not present")

