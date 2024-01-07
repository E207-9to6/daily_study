import math
daily, night, tree = map(int, input().split())

# 하루에 이만큼 올라가는 셈
per = daily-night

# 하루에 올라갈 수 있는 양 제외한 나머지
rest = tree - daily
print(math.ceil(rest/per)+1)