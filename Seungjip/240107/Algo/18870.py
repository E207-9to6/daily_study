N = int(input())
numbers = list(map(int, input().split()))
arr = set()
for num in numbers:
    arr.add((num))
arr = list(arr)
arr.sort()
# print(arr)
info = dict()
for idx in range(len(arr)):
    info[arr[idx]] = idx

for i in numbers:
    print(info[i], end=' ')