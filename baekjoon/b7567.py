dish = list(map(str, input().strip()))
prev = ""
ans = 0
for i in dish:
    if prev == i:
        ans += 5
    else:
        prev = i
        ans += 10

print(ans)