a = int(input())
c = 1
b = 0
while a != 0:
    v = int(input())
    a, v = v, a
    if v == a:
        c += 1
    if c > b:
        b = c
    if a != v:
        c = 1
print(b)
