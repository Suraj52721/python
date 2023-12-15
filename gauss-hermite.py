import numpy as np
import scipy.integrate as sp

def f(x):
    return x**2/((9+x**2)*(4+x**2))

def g(x):
    return np.exp(x**2)*f(x)

def quad(f, a, b):
    return sp.quad(f, a, b)[0]

def gauss_hermite(f, n):
    x, w = np.polynomial.hermite.hermgauss(n)
    return np.sum(w * f(x))

print("Quad: ", quad(f, -np.inf, np.inf))
print("Gauss-Hermite: ", gauss_hermite(g, 2))
print("Gauss-Hermite: ", gauss_hermite(g, 4))
print("Gauss-Hermite: ", gauss_hermite(g, 8))
print("Gauss-Hermite: ", gauss_hermite(g, 100))


