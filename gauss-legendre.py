import numpy as np
import scipy.integrate as sp

def f(x):
    return np.cos(3*x)/(5-4*np.cos(x))

def legendre(a,b,n):
    x,w = np.polynomial.legendre.leggauss(n)
    return (b-a)/2*np.sum(w*f((b-a)/2*x+(b+a)/2))

def quad(a,b):
    return sp.quad(f,a,b)[0]


print(f'Analytical Quad Value = {quad(0,2*np.pi)}')
print(legendre(0,2*np.pi,4))
print(legendre(0,2*np.pi,5))
print(legendre(0,2*np.pi,6))
print(legendre(0,2*np.pi,10))

