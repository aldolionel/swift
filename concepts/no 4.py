import scipy.special
import math

def hitung(n):
    x = []
    for i in range(4):
        y = (scipy.special.binom(n, i) * math.pow(5,n-i)) / math.pow(6, n)
        x.append(y)
    return(1 - sum(x))

print(round(hitung(8), 4))