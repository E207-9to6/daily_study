N = int(input())
arr = set()

for i in range(N):
    word = input()
    k = len(word)
    arr.add((k, word))
arr = list(arr)
arr.sort()
for j in arr:
    print(j[1])