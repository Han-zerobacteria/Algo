n = int(input())
a = list(map(str, input().strip()))
A_score = 0
B_score = 0
for i in a:
    if i == "A":
        A_score += 1
    else:
        B_score += 1

if A_score > B_score:
    print("A")
elif B_score > A_score:
    print("B")
else:
    print("Tie")