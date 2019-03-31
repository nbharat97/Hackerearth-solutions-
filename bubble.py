N = input()
k = input()
a =[]

for i in range(0,N):
    a.append(input())

for i in range(0,N):
    for j in range(0,N-1):
        if ((a[j]%k)>(a[j+1]%k)):

            
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t

print(a)
