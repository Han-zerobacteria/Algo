now_t, now_m, now_s = map(str, input().split(":")) 
t, m, s = map(str, input().split(":")) 
now = now_t + now_m + now_s
start = t + m + s
print(now, start)