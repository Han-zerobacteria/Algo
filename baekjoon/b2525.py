a, b = map(int, input().split())
c = int(input())

ans_t = a
ans_m = b + c

while ans_m >= 60:
    ans_m -= 60
    ans_t += 1

ans_t %= 24   # 하루 넘어가는 처리

print(ans_t, ans_m)
