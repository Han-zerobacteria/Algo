max_int = 0
ans = 0
for i in range(1, 10):
    a = int(input())
    if max_int < a:
        max_int = a
        ans = i

print(max_int)
print(ans) 