N = int(input())
in_room = []
for _ in range(N):
    name, state = input().split()
    if state == 'enter':
        in_room.append(name)
    else:
        in_room.remove(name)

in_room.sort(reverse=True)
for each in in_room:
    print(each)