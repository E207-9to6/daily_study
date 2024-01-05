A = int(input())
B = int(input())
C = int(input())

if A + B + C !=180:
    print("Error")
elif len({A, B, C}) == 3:
    print("Scalene")
elif len({A, B, C}) == 2:
    print("Isosceles")
else:
    print("Equilateral")