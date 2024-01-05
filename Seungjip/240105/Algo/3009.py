a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
width = [a, c, e]
height = [b, d, f]

fw = 0
fh = 0

for w in width:
    if width.count(w) == 1:
        fw = w

for h in height:
    if height.count(h) == 1:
        fh = h

print(fw, fh)