import math

def compute_e(n):
    return math.exp(n * math.log((1 + 1/n)))

for i in range(20):
    ec = compute_e(10**i)
    print('e cumputed: %0.50f' % ec)

er = math.e
print('Actual e :', er)
