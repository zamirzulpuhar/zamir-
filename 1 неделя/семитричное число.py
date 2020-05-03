num = int(input())
units = num % 10
dozens = num // 10 % 10
undo = int(units * 10 + dozens)
thh = int(num // 100)
print(undo - thh + 1)
