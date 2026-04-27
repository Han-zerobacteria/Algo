t = int(input())
for _ in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in li:
        ans += i

    print(ans)