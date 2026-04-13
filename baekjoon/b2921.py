'''
모든 경우의 수를 찾아라
ex) input 2
-> (0, 0), (0, 1), (1, 2), (2, 2)
-> 12
'''
# 이중 for문
n = int(input())
ans = 0
for i in range(n+1):
    for j in range(i, n+1):
        ans += (i + j)
print(ans)

# 이중 for문 없이
# n = int(input())
# print(((n) * (n+1) * (n+2)) // 2)