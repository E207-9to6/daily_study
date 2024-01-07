import sys
input = sys.stdin.readline
arr = []

N = input()
for chr in N:
    arr.append(chr)
arr.pop()
arr = list(map(int, arr))
arr.sort(reverse=True)
arr = list(map(str, arr))
print(''.join(arr))