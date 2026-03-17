'''
M 이상 N 이하 중 완전 제곱수
첫째 줄 그합 둘째 줄 그중 최솟값
'''

m = int(input())
n = int(input())

i = 1
l = []

while True:
    if i * i >= m and i*i <= n:
        l.append(i*i)
    elif i*i > n:
        break
    i += 1
if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))