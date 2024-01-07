import sys
input = sys.stdin.readline
N = int(input())
numbers = []
for _ in range(N):
    K = int(input())
    numbers.append(K)

numbers.sort()
for i in numbers:
    print(i)