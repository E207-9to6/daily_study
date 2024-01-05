a, b, c = map(int, input().split())
sides = [a, b, c]
sides.sort()
while sides[0]+sides[1] <= sides[2]:
    sides[2] -= 1
    sides.sort()
print(sum(sides))