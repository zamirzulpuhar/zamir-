s = list(map(int, input().split(" ")))
s2 = []
for i in range(len(s)):
    if i % 2 == 0:
        s2.append(s[i])
print(' '.join(map(str, s2)))
