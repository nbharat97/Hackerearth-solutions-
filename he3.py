T = int(input())

for k in range(0,T):
    N = int(input())
    A = []
    B = []
    for i in range(0,N):
        A.append(int(input()))
    
    for i in range(0,N):
        for j in range(0,N):
            B.append(abs(A[i] - A[j]) + abs(i - j))
            
    print(max(B))
