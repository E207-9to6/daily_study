import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

counter = Counter(numbers)
final = [counter[num] if num in counter else 0 for num in checks]

print(*final)
