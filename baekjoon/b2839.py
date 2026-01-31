''' 
N : 배달해야되는 무게
3, 5로 최소 값 만들기
최소 봉지 갯수 출력
최소 봉지 수로 배달
'''
# 내 풀이
# N = int(input())
# a = b = 0
# ans = float('inf')
# for a in range(1, N+1):
#     for b in range(1, N+1):
#         if (5 * a) + (3 * b) == N:
#             ans = min(ans, (a + b))
#         else:
#             ans = -1
# print(ans)

'''
완전 탐색
N = int(input())
ans = float('inf')

for a in range(N // 5 + 1):
    for b in range(N // 3 + 1):
        if 5 * a + 3 * b == N:
            ans = min(ans, a + b)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
'''

N = int(input())
ans = 0

while N >= 0:
    if N % 5 == 0:
        ans += N // 5
        print(ans)
        break
    N -= 3
    ans += 1
else:
    print(-1)