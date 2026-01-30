'''
변의 길이 1인  정사각형 n개
만들 수 있는 직사각형 갯수
A 
'''

# n = int(input())
# ans = 0
# arr = []
# for r in range(1, n + 1):
#     for c in range(1, n + 1):
#         if r * c <= n :
            
#             arr.append(r * c)
#             ans += 1
#             print(arr)
# print(ans)

N = int(input())

ans = 0
for i in range(1, N + 1):
    for j in range(i, N + 1):
        if i*j <= N:
            ans += 1
print(ans)