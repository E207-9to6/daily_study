import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    a = int(input())
    arr.append(a)
arr.sort()
for i in arr:
    print(i)