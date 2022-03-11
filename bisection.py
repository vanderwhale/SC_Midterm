import math

def f(x) :
    y = x - x**3/math.factorial(3) + x**5/math.factorial(5) - x**7/math.factorial(7) + x**9/math.factorial(9) - x**11/math.factorial(11) + x**13/math.factorial(13) - x**15/math.factorial(15) + x**17/math.factorial(17) - x**19/math.factorial(19) + x**21/math.factorial(21) - x**23/math.factorial(23) + x**25/math.factorial(25) - x**27/math.factorial(27) + x**29/math.factorial(29) - x**31/math.factorial(31) + x**33/math.factorial(33)
    return y

a = 3
b = 4
e = 0.000000000000001

def bisection(a,b,e) :
    step = 1
    condition = True

    while condition:
        c = (a+b)/2
        (step, c, f(c))

        if f(a) * f(c) < 0:
            b = c

        else:
            a = c
        step = step + 1
        condition = abs(f(c)) > e

    print('Computed pi is : %0.15f' % c)
    print('Actual pi is   : 3.141592653589793')

bisection(a,b,e)
