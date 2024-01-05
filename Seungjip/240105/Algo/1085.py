px, py, sx, sy = map(int, input().split())
print(min(px, py, sx-px, sy-py))