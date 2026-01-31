''' 
n : 인원 수
'''
n = int(input())
arr = sorted(map(int, input().split()))
ans = a = 0
for i in range(len(arr)):
    a += arr[i]
    ans += a
print(ans)
