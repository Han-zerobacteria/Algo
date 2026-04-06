t = int(input())
for _ in range(t):
    ans = 0
    s = int(input())
    ans += s
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        ans += q * p
    print(ans)
    