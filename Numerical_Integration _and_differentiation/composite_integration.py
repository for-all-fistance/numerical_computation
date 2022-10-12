# composite integration
import numpy as np
def trapezoid(f,a,b):    			# trapezoid(n=1)
    return (b-a)*(f(b)+f(a))/2

def compositeInt_trape(f,a,b,n):    # recursive composite integration
    eps = 1e-10
    val = trapezoid(f,a+eps,b)
    print('T1: %.7f' % (val))
    i = 1
    while i<=np.log2(n):
        h = (b-a)/(2**i)
        t = 0
        for k in range(1,2**(i-1)+1):
            xkc = a + (2*k-1)*h
            t += f(xkc)*h
        val = val/2 + t
        print('T%d: %.7f' % (2**i,val))
        i += 1
    return val

if __name__ == '__main__':
    a = 0
    b = 1
    f = lambda x: np.sin(x)/x
    n = 3
    val = compositeInt_trape(f, a, b, 2**n)
    print('recursive trapezoid: %.7f' % (val))
