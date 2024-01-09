import sys

N, M = map(int, sys.stdin.readline().split())
poketmons = {}
answers = []
for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    poketmons[name] = i
    poketmons[i] = name

for _ in range(M):
    query = sys.stdin.readline().strip()
    if query.isdigit():
        answers.append(poketmons[int(query)])
    else:
        answers.append(poketmons[query])

print('\n'.join(map(str, answers)))
