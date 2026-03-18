n = int(input())
for _ in range(n):
    m = int(input())
    max_price = 0
    ans = ""
    for _ in range(m):
        price, player = input().split()
        price = int(price)
        if max_price < price:
            max_price = price
            ans = player
    print(ans)