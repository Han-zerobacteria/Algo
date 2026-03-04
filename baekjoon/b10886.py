n = int(input())
cute = 0
not_cute = 0
for i in range(n):
    request = int(input())
    if request == 0:
        not_cute += 1
    else:
        cute += 1

if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")