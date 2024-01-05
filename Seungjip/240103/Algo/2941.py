string = input()
cr_alp = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}
i = 0
cnt = 0


# 인덱스를 하나씩 순회할 것:
while i < len(string):
    # 마지막이라면 1증가시키고 종료
    if i == len(string)-1:
        cnt += 1
        break

    if i < len(string)-2 and string[i:i+3] == "dz=":
        cnt += 1
        i += 3
    elif i < len(string)-1 and string[i:i+2] in cr_alp:
        cnt += 1
        i += 2
    else :
        cnt += 1
        i += 1

print(cnt)