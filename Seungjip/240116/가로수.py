N = int(input())
trees = []
for _ in range(N):
    tree = int(input())
    trees.append(tree)
divs = []
for ind in range(N-1):
    div = trees[ind+1] - trees[ind]
    divs.append(div)


def getdivision(a, b):
    n1 = a
    n2 = b
    while n2 != 0:
        temp = n1
        n1 = n2
        n2 = temp%n2
    return n1

# print(divs)

start = divs[0]

for i in range(1, N-1):
    temp = getdivision(start, divs[i])
    start = temp

# print(start)

ans = 0
for i in divs:
    ans += i//start -1

print(ans)