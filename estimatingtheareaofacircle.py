# Kattis-Python-Solutions
# Coded Daniyal Arteshdar 
import sys, math
while True:
    inp = inp = [float(i) for i in sys.stdin.readline().split()]
    if inp[0] == 0 and inp[1] == 0 and inp[2] == 0: break
    else:  
        actual = math.pi*(inp[0]**2)
        estimate = (inp[2] * 2 * inp[0] * 2 * inp[0]) / inp[1];
    print(actual, estimate) 
