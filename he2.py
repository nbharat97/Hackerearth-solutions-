N = int(input())
A = []
B = []
C = []

for i in range(0,N):
    A.append(int(input()))

for i in range(0,N):
    B.append(int(input()))

for i in range(0,N):
    C.append(A[i] + B[i])
for i in C:
    print(i,end=" ")

