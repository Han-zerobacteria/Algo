'''
N : 한줄 좌석 수
S : 일반 좌석
L : 커플 석(L은 항상 두개씩 쌍으로)
컵 홀더 양옆 배치 but 커플 석 사이엔 컵홀더 X
'''

'''
틀린 풀이
n = int(input())
arr = list(map(str, input()))
cnt = 2
for i in range(n):
    if arr[i] == "S":
        cnt += 1
    elif arr[i] == "L":
        cnt += 0.5
print(int(cnt))
'''
n = int(input())
seat = input()

# 기본 컵홀더 개수
holder = n + 1

# 커플석 개수만큼 컵홀더 감소
holder -= seat.count("LL")

# 사람 수보다 컵홀더가 많아도 의미 없음
print(min(n, holder))
