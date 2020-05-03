h = - 1
n = 0
m = 0
while h != 0:
    h = int(input())
    if h > n and h != 0:
        m = n
        n = h
    elif h > m and h != 0:
        m = h
print(m)
