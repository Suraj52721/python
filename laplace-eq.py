import numpy as np
import matplotlib.pyplot as plt
h = 5
xi,yi = 0,50
xf,yf = 75,100
accuracy = 20

print('initial temperature at x = 0 is',xi)
print('initial temperature at y = 0 is',yi)
print('final temperature at x = 75 is',xf)
print('final temperature at y = 100 is',yf)
print('accuracy is',accuracy)

n = int((xf-xi)/h)
print('number of nodes in x and y direction is',n)
m = np.zeros((n,n))
#defining boundary conditions
for a in range(1,n-1):
    m[a][0]=xi
    m[a][n-1]=xf
    m[n-1][a]=yi
    m[0][a]=yf

for t in range(accuracy):
    for i in range(1,n-1):
        for j in range(1,n-1):
            m[i][j] = (m[i+1][j]+m[i-1][j]+m[i][j+1]+m[i][j-1])/4
      
print(m)

#heat map
plt.imshow(m)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Heat Map of Laplace Equation')
plt.show()
