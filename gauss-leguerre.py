import numpy as np
import scipy.integrate as sp

def f(x):
    return x**2/(1+x**3)

def g(x):
    return np.exp(-x)*(x**2/(1+x**3))

def gauss_leguerre(f, n):
    x, w = np.polynomial.legendre.leggauss(n)
    return np.sum(w * f(x))

def quad(f, a, b):
    return sp.quad(f, a, b)[0]


print("scipy.integrate.quad: ", quad(f, 0, np.inf))
print("Gauss-Legendre: ", gauss_leguerre(g, 4))
print("Gauss-Legendre: ", gauss_leguerre(g, 6))
print("Gauss-Legendre: ", gauss_leguerre(g, 8))
print("Gauss-Legendre: ", gauss_leguerre(g, 10))

