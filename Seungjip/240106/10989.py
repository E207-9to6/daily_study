import sys
input = sys.stdin.readline

N=int(input())
arr = []
for _ in range(N):
    K=int(input())
    arr.append(K)
arr.sort()
for i in arr:
    print(i)