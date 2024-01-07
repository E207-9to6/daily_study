N = int(input())
arr = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    arr.append((age, i, name))

arr.sort()
for j in arr:
    print(j[0], j[2])