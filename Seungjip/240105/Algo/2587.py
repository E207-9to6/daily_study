arr = []
for _ in range(5):
    a = int(input())
    arr.append(a)
arr.sort()
print(sum(arr)//5)
print(arr[2])