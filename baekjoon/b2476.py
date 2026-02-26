n = int(input())
ans = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    dice = [0] * 7
    dice[a] += 1
    dice[b] += 1
    dice[c] += 1
    money = 0
    
    for i in range(1, 7):
        if dice[i] == 3:
            money = 10000 + (i * 1000)
            break
        elif dice[i] == 2:
            money = 1000 + (i * 100)
            break
    else:
        money = max(a, b, c) * 100

    ans = max(ans, money)

print(ans)