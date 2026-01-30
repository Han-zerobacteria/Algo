'''
L : 케이크 길이
N : 방청객 인원 수
가장 왼쪾 1번 오른쪾 L
원하는 조각 P ~ K
이미 적혀 있는 조각 X
'''

L = int(input())
N = int(input())

rollCake = [0] * (L + 1)
received = [0] * (N + 1)

max_want = cnt = 0 
for i in range(1, N+1):
    P, K = map(int, input().split())
    if K - P > cnt:
        cnt = K - P 
        max_want = i
    
    for j in range(P, K+1):
        if rollCake[j] == 0:
            rollCake[j] += 1
            received[i] += 1
    


print(max_want)
print(received.index(max(received)))