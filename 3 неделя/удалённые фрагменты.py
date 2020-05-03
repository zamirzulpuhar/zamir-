s = input()
X = 'h'
n = len(s)
Y = s[::-1]
K = s.find(X)
L = Y.find(X)
LF = n - L - 1
print(s[0:K], s[LF + 1:], sep='')
