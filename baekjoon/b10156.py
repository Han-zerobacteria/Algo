'''
K : 과자 개당 가격
N : 사려하는 과자 갯수 
M : 현재 가진 돈
'''

n, m, k = map(int, input().split())

ans = (n * m) - k
if ans < 0:
    ans = 0
print(ans)