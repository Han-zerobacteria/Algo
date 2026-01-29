a = input()
alpa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for x in alpa:
    a = a.replace(x, "*")

print(len(a))
