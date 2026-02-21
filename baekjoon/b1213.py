name = input().strip()

# 1. 문자 개수 세기
count = {}

for ch in name:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

odd_count = 0
mid = ""
left = ""

# 2. 알파벳 순으로 처리
for ch in sorted(count.keys()):
    if count[ch] % 2 == 1:
        odd_count += 1
    left += ch * (count[ch] // 2)
# 3. 팰린드롬 가능 여부 판단
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    print(left + mid + left[::-1])