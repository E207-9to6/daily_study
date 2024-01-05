N = int(input())
width = []
height = []
for _ in range(N):
    a, b = map(int, input().split())
    width.append(a)
    height.append(b)

fw = max(width) - min(width)
fh = max(height) - min(height)
print(fw*fh)