# Kattis-Python-Solutions
# Coded by Daniyal Arteshdar

def getSum(n):
    sm = 0
    for digit in str(n):
        sm += int(digit)
    return sm

num  = int(input())
x = 0

while True:
    if (num % getSum(num) == 0):
        print(num)
        break
    else:
        num = num + 1

