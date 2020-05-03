a = int(input())
b = int(input())
div = a % b
check = ((div + 1) % 2) - div
print(("YES" * check), end="")
print(("NO" * (((check + 1) % check) - check)), end="")
