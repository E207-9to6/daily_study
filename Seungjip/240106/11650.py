N = int(input())
A = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append((a,b))
A.sort()
for i in range(len(A)):
    print(*A[i])