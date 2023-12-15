import numpy as np
import matplotlib.pyplot as plt
h = 0.1
xi,yi = 0,1
xf= 1
accuracy = 10

def y(x,i):
    if x==0:
        return yi
    elif x==1-h:
        return (m[-2] + m[i-1])/(2+h**2)
    else:
        return (m[i+1] + m[i-1])/(2+h**2)

n = int((xf-xi)/h)
print(f'n = {n}')
m = np.zeros(n)
m[0] = y(xi,0)

t = np.zeros(n)
for j in range(accuracy):
    for i in range(1,n):
        m[i] = y(xi+i*h,i)      
    t=m
print(f'Solution Matrix: {m}') 

x = np.linspace(xi,xf,n)
plt.plot(x,m)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Reaction Diffusion equation')
plt.show()




