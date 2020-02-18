i = 0
num = 1000
while i < 25:
    num -= 1
    if num % 7 == 0 or num % 9 == 0:
        print(num)
        i += 1
