N = int(input())
cnt = N

for _ in range(N):
    string = input()
    for i in range(len(string)-2):
        if string[i] == string[i+1]:
            pass
        elif string[i] in string[i+2:]:
            cnt -=1
            break

print(cnt)