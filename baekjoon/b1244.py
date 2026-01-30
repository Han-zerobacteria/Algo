N = int(input())
arr = [0] + list(map(int, input().split()))
M = int(input())
for _ in range(M):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(num, N+1, num):
            arr[i] = (arr[i] + 1) % 2
    else:
        arr[num] = (arr[num] + 1) % 2
        j = 1
        while 1 <= num-j and num+j <= N and arr[num-j] == arr[num+j]:
            arr[num-j] = (arr[num-j] + 1) % 2
            arr[num+j] = (arr[num+j] + 1) % 2
            j += 1
for i in range(1, N+1, 20):
    print(
        ' '.join([str(n) for n in arr[i:i+20]]))
