while True:
    a, b, c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    sides = [a, b, c]
    sides.sort()
    if sides[0] + sides[1] <= sides[2]:
        print("Invalid")
        continue
    if len({a, b, c})==3:
        print("Scalene")
    elif len({a, b, c})==2:
        print("Isosceles")
    else:
        print("Equilateral")